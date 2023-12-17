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

def scrape_jobs(query):
    driver = webdriver.Chrome()
    driver.get("https://www.geeksforgeeks.org/") 
    

    input_search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[1]/div[2]/span/span/span[1]/input')
    input_search.send_keys(query)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='RA-root']/div/div[1]/div[1]/div[2]/span/span/span[2]/button")))
    button = driver.find_element(By.XPATH, '//*[@id="RA-root"]/div/div[1]/div[1]/div[2]/span/span/span[2]/button')
    button.click()

scrape_jobs('java developer inteerview questions')   