from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from jobspark.settings import CHROME_DRIVER_PATH
from webdriver_manager.chrome import ChromeDriverManager

def scrape_jobs(query):
    # Install and manage ChromeDriver
    driver_path = ChromeDriverManager().install()

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode

    # Initialize Chrome driver with options
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    # Open the TimesJobs website
    driver.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation=India")

    try:
        # Close any popup that might appear
        driver.find_element(By.XPATH, '//*[@id="closeSpanId"]').click()
    except Exception as e:
        print('Exception occurred:')

    # Enter the search query
    input_search = driver.find_element(By.XPATH, '//*[@id="txtKeywords"]')
    input_search.send_keys(query)

    # Click the search button
    button = driver.find_element(By.XPATH, '//*[@id="quickSearchBean"]/button').click()

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

    # Print the extracted data
    for job_data in data_dict_list:
        print(job_data)

    # Close the browser
    driver.quit()

    return data_dict_list if data_dict_list else None
