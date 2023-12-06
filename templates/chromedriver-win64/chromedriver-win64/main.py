from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

# Set up the Selenium Chrome driver
service = Service('path_to_chromedriver')  # Replace 'path_to_chromedriver' with the actual path to the chromedriver executable
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.naukri.com/python-developer-jobs?k=python%20developer"
driver.get(url)

# Wait for the job postings to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobTuple")))

# Scroll to the bottom of the page to load all job postings
scroll_pause_time = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get the page source after all job postings have been loaded
page_source = driver.page_source

# Close the driver
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find all job postings
job_postings = soup.find_all("li", class_="jobTuple")

# Iterate over the job postings and extract the desired information
for job_posting in job_postings:
    job_title = job_posting.find("a", class_="title").text.strip()
    company_name = job_posting.find("a", class_="subTitle").text.strip()
    location = job_posting.find("li", class_="location").text.strip()
    salary = job_posting.find("li", class_="salary").text.strip()
    experience = job_posting.find("li", class_="experience").text.strip()
    
    print("Job Title:", job_title)
    print("Company Name:", company_name)
    print("Location:", location)
    print("Salary:", salary)
    print("Experience:", experience)
    print("----------")