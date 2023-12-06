from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from jobspark.settings import CHROME_DRIVER_PATH
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Add any other options you need

    service = webdriver.Chrome(service_args=["--verbose"], executable_path=ChromeDriverManager().install(), options=options)
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)  # Pass options to Chrome

    return driver

def search_jobs(driver, query):
    driver.get("https://www.naukri.com/") 

    input_search = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div[1]/div[1]/div/input')
    input_search.send_keys(query)
    button = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[6]').click()

    # Wait for the job postings to load
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "styles_jlc__main__VdwtF")))

def scrape_data(driver):
    # Retrieve all the job posting elements
    posting_elements = driver.find_elements(By.XPATH, "//*[@id='listContainer']/div[2]/div[contains(@class,'styles_jlc__main__VdwtF')]")

    job_data_list = []

    for job_posting in posting_elements:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        post = soup.find_all('div', 'cust-job-tuple layout-wrapper lay-2 sjw__tuple')

        for i in post:
            data_dict = {}
            
            JobTitle = i.find('a')
            data_dict['JobTitle'] = JobTitle.text
            ExperienceReqd = i.find('span', class_='exp-wrap')
            data_dict['ExperienceReqd'] = ExperienceReqd.text if i.find('span', class_='date') else 'not specified'

            data_dict['SalaryRange'] = i.find('span', class_='sal-wrap ver-line').text
            data_dict['City'] = i.find('span', class_='loc-wrap ver-line').text
            data_dict['Description'] = i.find('span', class_='job-desc ni-job-tuple-icon ni-job-tuple-icon-srp-description').text
            data_dict['Company'] = i.find('span', class_='comp-dtls-wrap').text
            data_dict['Rating'] = i.find('span', class_='star-rating').text if i.find('span', class_='star-rating') else "Not Rated"
            data_dict['DatePosted'] = i.find('span', class_='date').text if i.find('span', class_='date') else None
            data_dict['Site'] = 'Naukri'
            data_dict['URL'] = 'URL_of_the_job_posting'  # Replace with the actual URL
            # Add other fields as needed
            
            # Append the dictionary to the list
            job_data_list.append(data_dict)
            for job in job_data_list:
                print(job)

    return job_data_list

def main(query):
    driver = initialize_driver()
    search_jobs(driver, query)
    job_data = scrape_data(driver)
    driver.quit()
    return job_data

