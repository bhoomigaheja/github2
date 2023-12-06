from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
import os

def open_website():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--headless')
    
    # Check if the environment variable is set
    google_chrome_bin = os.environ.get("GOOGLE_CHROME_BIN")
    if google_chrome_bin:
        chrome_options.binary_location = google_chrome_bin
    else:
        print("GOOGLE_CHROME_BIN environment variable not set.")
        # You may want to handle this case based on your requirements

    ScriptDir = os.path.abspath(os.path.dirname(__file__))
    user_data_dir = os.path.join(ScriptDir, 'chromedata')

    chrome_options.add_argument(f"user-data-dir={user_data_dir}")

    # Use ChromeDriverManager to automatically download and manage ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Initialize Chrome driver with options
    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()

    return driver, chrome_options  # Return both the driver and chrome_options


    

def website(driver):
    driver.get("https://flowgpt.com/chat") 
    while True:
        try:
            Xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea'
            driver.find_element(by=By.XPATH, value=Xpath)
            break
        except:
            pass

def send(driver, query):
    Xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea'
    driver.find_element(by=By.XPATH, value=Xpath).send_keys(query)
    button_xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button'
    driver.find_element(By.XPATH, value=button_xpath).click()
    sleep(80)  # Adjusted sleep time

def text(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    result = soup.find('div', class_='max-w-[62vw] md:w-full css-0')

    parent_div = soup.find('div', {'class': 'flowgpt-markdown prose-invert markdown-body flex-1 overflow-auto whitespace-pre-wrap text-fgMain-200'})
    list_items = soup.find_all('li')
    scraped_text = [item.text.strip() for item in list_items]
    print(f"a:{scraped_text}")
    return scraped_text

def popup(driver):
    try:
        # Find and click the element to close the popup
        xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/button'
        driver.find_element(by=By.XPATH, value=xpath).click()
    except Exception as e:
        print('Exception occurred during popup closing:', str(e))
def popup2(driver):
    try:
        # Find and click the element to close the popup
        xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/button'
        driver.find_element(by=By.XPATH, value=xpath).click()
    except Exception as e:
        print('Exception occurred during popup closing:', str(e))
   
def gpt(query):
    result = open_website()

    if result is not None and isinstance(result, tuple) and len(result) == 2:
        driver, chrome_options = result
        website(driver)
        popup2(driver)
        send(driver, query)
        scraped_text = text(driver)  # Assuming text() returns the scraped text as a list
        sleep(5)  
        popup(driver)
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
