from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
import os
import pathlib
from time import sleep
from selenium.webdriver.chrome.service import Service

def open_website(url):
    try:
        ScriptDir = pathlib.Path().absolute()
        chrome_options = Options()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_options.add_argument(f"user-data-dir={ScriptDir}\\chromedata")
        #chrome_options.add_argument('--headless')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        return driver
    except Exception as e:
        print(f"Error in open_website function: {e}")
        return None 

def scrape_jobs(query):
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation=India"

    # Open the website
    driver = open_website(url)

    try:
        # Close any popup that might appear
        driver.find_element(By.XPATH, '//*[@id="closeSpanId"]').click()
    except Exception as e:
        print('Exception occurred:')

    # Enter the search query
    input_search = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/form/div[1]/input')
    input_search.send_keys(query)

    # Click the search button
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/form/button').click()

    try:
        # Close any popup that might appear
        driver.find_element(By.XPATH, '//*[@id="closeSpanId"]').click()
    except Exception as e:
        print('Exception occurred:')

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'lxml')
    result = soup.find('ul', class_='new-joblist')
    result2 = result.find_all('li', class_='clearfix job-bx wht-shd-bx')

    data_dict_list = []  # List to store dictionaries

    # Extract job details
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
        Mat_icons = i.find('i', class_='material-icons')
        Exp = Mat_icons.next_sibling.text.strip()
        data_dict['experience'] = Exp

        # City
        spans = i.find('span')
        City = spans.text
        data_dict['city'] = City

        # Date Posted
        Date = i.find('span', class_='sim-posted')
        Date = Date.text.strip()
        data_dict['date'] = Date

        # URL
        URL = i.find('a').get('href')
        data_dict['url'] = URL

        data_dict_list.append(data_dict)

    # Print the extracted data
    for job_data in data_dict_list:
        print(job_data)

    # Close the browser
    \
    return data_dict_list if data_dict_list else None
    driver.quit()

# Example usage
