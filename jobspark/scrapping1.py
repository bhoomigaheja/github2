import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from jobspark.settings import CHROME_DRIVER_PATH

def scrape_jobs(query):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options) 
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)  # Pass options to Chrome
  # Pass options to Chrome

   
    driver.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation=India") 
    try:
        driver.find_element(By.XPATH, '//*[@id="closeSpanId"]').click()
    except Exception as e:
        print('Exception occurred:')

    input_search = driver.find_element(By.XPATH, '//*[@id="txtKeywords"]')
    input_search.send_keys(query)

    button = driver.find_element(By.XPATH, '//*[@id="quickSearchBean"]/button').click()
    try:
        driver.find_element(By.XPATH, '//*[@id="closeSpanId"]').click()
    except Exception as e:
        print('Exception occurred:')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    result = soup.find('ul', class_='new-joblist')
    result2 = result.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
    data_dict_list = []  # List to store dictionaries
    
    for i in result2:
        data_dict = {}  # Dictionary to store data for each job
        
        # TITLE
        title = i.find('a')
        data_dict['title'] = title.text

        # Description
        description = i.find('label').next_sibling.strip()
        data_dict['description'] = description

        # COMPANY
        text = i.find('h3', class_='joblist-comp-name')
        text = text.text
        initial_company = text.find('(')
        Company = text[:initial_company]
        Company = Company.strip()
        data_dict['company'] = Company

        # Exp
        Mat_icons = i.find_all('i', class_='material-icons')
        Exp = Mat_icons[0].next_sibling.text.strip()
        data_dict['experience'] = Exp

        # City
        spans = i.find_all('span')
        City = spans[1].text
        data_dict['city'] = City

        # Date Posted
        Date = i.find('span', class_='sim-posted')
        Date = Date.text.strip()
        data_dict['date'] = Date

        # URL
        URL = i.find('a').get('href')
        data_dict['url'] = URL

        data_dict_list.append(data_dict)

    for job_data in data_dict_list:
        print(job_data)

    driver.quit()

    return data_dict_list if data_dict_list else None
