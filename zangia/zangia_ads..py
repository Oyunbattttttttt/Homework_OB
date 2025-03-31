# selenium - pip install selenium
# chromedriver 

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from joblib import Parallel, delayed # pip install joblib


def collect_data(driver):
    data = {}
    data['title'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/h3').text
    data['company'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[1]/div[1]/div[2]/p').text
    data['wage'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[1]/div').text
   
    try:
        data['location'] = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[5]/div/div[1]/span').text
    
    except:
        try:
            data['location'] = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[4]/div/div[1]/span').text
        except:
            data['location'] = None  # Or empty string "" if you prefer

    try:
        data['sector'] = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[5]/div/div[2]/span').text
    
    except:
        try:
            data['sector'] = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[4]/div/div[2]/span').text
        except:
            data['sector'] = None  # Or empty string "" if you prefer


    try:
        data['level'] = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[5]/div/div[3]/span').text
    
    except:
        try:
            data['level'] = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[4]/div/div[3]/span').text
        except:
            data['level'] = None  # Or empty string "" if you prefer

    return data 



def collect_ad(ad_number):
    main_url = 'https://www.zangia.mn/'

    driver = webdriver.Chrome()
    driver.get(main_url)

    driver.find_element(By.XPATH, f"/html/body/div[2]/div[2]/div/div[3]/div[3]/div[1]/div[{ad_number}]/div[2]/a").click()

    data = collect_data(driver)

    return data

ad_list = range(1,81)

results = Parallel(n_jobs=2)(delayed(collect_ad)(n) for n in ad_list)
# Save to dataframe
df = pd.DataFrame(results)  
# Save to csv
df.to_csv('zangia/unegui_ads_1.csv', index=False, encoding='utf-8-sig') 