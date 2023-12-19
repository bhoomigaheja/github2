from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import pathlib
def open_website():
    try:
        chrome_options = webdriver.ChromeOptions()
    
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        ScriptDir = pathlib.Path().absolute()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_options.add_argument(f"user-data-dir={ScriptDir}\\chromedata")
        
    # Check if the environment variable is set
        
        # You may want to handle this case based on your requirements

    # Use ChromeDriverManager to automatically download and manage ChromeDriver
        service = Service(ChromeDriverManager().install())

    # Initialize Chrome driver with options
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.maximize_window()

        return driver, chrome_options
    except Exception as e:
        print(f"Error in open_website function: {e}")
        return None 



def website(driver):
    driver.get("https://flowgpt.com/chat") 
    while True:
        try:
            Xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea'
            driver.find_element(by=By.XPATH, value=Xpath)
            break
        except:
            pass
        try:
            driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div/button').click()
        except Exception as e:
            print('Exception occurred:')

        sleep(20)

def send(driver, query):
    Xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea'
    driver.find_element(by=By.XPATH, value=Xpath).send_keys(query)
    button_xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button'
    driver.find_element(By.XPATH, value=button_xpath).click()
    sleep(20)  # Adjusted sleep time

def text(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    result = soup.find('div', class_='max-w-[62vw] md:w-full css-0')

    parent_div = soup.find('div', {'class': 'flowgpt-markdown prose-invert markdown-body flex-1 overflow-auto whitespace-pre-wrap text-fgMain-200'})
    list_items = soup.find_all('li')
    scraped_text = [item.text.strip() for item in list_items]
    print(f"a:{scraped_text}")
    return scraped_text




   
def gpt(query):
    result = open_website()

    if result is not None and isinstance(result, tuple) and len(result) == 2:
        driver, chrome_options = result
        website(driver)
        
        send(driver, query)
        scraped_text = text(driver)  # Assuming text() returns the scraped text as a list
        sleep(5)  
       
        # Return the scraped data as a dictionary
        scraped_data = {'scraped_text': scraped_text}
        print(f"b: {scraped_data}")

        # Close the driver
        driver.quit()

        return scraped_data
    else:
        print("Error in open_website function. Check the implementation.")
        return {'error': 'Failed to open the website'}

    return scraped_data

gpt('java')