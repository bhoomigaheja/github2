import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from jobspark.settings import CHROME_DRIVER_PATH

# Initialize an empty list to store job data dictionaries
job_data_list2 = []

def scrape_data2(query2):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)  # Pass options to Chrome

    driver.get("https://www.naukri.com/") 

    input_search = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div[1]/div[1]/div/input')
    input_search.send_keys(query2)
    button = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[6]').click()

    # Wait for the job postings to load
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "styles_jlc__main__VdwtF")))

    # Retrieve all the job posting elements
    posting_elements = driver.find_elements(By.XPATH, "//*[@id='listContainer']/div[2]/div[contains(@class,'styles_jlc__main__VdwtF')]")

    for job_posting in posting_elements:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))
        elements = driver.find_elements(By.XPATH, "//*[@id='listContainer']/div[2]/div/div[1][contains(@class,'srp-jobtuple-wrapper')]")
    
        for job_posting in posting_elements:
            wait = WebDriverWait(driver, 30)
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='listContainer']/div[2]/div/div[1]/div[contains(@class,'cust-job-tuple layout-wrapper lay-2 sjw__tuple')]")))
            soup = BeautifulSoup(driver.page_source, 'lxml')
            post = soup.find_all('div', 'cust-job-tuple layout-wrapper lay-2 sjw__tuple')

            for i in post:
                data_dict2 = {}
                
                JobTitle = i.find('a')
                data_dict2['JobTitle'] = JobTitle.text
                ExperienceReqd = i.find('span', class_='exp-wrap')
                data_dict2['ExperienceReqd'] = ExperienceReqd.text if i.find('span', class_='date') else 'not specified'

                data_dict2['SalaryRange'] = i.find('span', class_='sal-wrap ver-line').text
                data_dict2['City'] = i.find('span', class_='loc-wrap ver-line').text
                data_dict2['Description'] = i.find('span', class_='job-desc ni-job-tuple-icon ni-job-tuple-icon-srp-description').text
                data_dict2['Company'] = i.find('span', class_='comp-dtls-wrap').text
                data_dict2['Rating'] = i.find('span', class_='star-rating').text if i.find('span', class_='star-rating') else "Not Rated"
                data_dict2['DatePosted'] = i.find('span', class_='date').text if i.find('span', class_='date') else None
                data_dict2['Site'] = 'Naukri'
                data_dict2['URL'] = 'URL_of_the_job_posting'  # Replace with the actual URL
                # Add other fields as needed
                
                # Append the dictionary to the list
                job_data_list2.append(data_dict2)
                for job in job_data_list2:
                    print(job)
                
    # Now, job_data_list contains a list of dictionaries, each representing a job posting
    # You can further process or save this data as needed
    
    # Close the browser
    driver.quit()
    return job_data_list2

