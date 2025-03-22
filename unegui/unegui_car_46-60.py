# selenium - pip install selenium
# chromedriver 

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from joblib import Parallel, delayed # pip install joblib


def collect_data(driver):
    data = {}
    data['title'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/h1').text
    data['location'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/a/span').text
    data['date'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]').text
    data['id'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[2]/span').text
    data['price'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/section[1]/div/div[3]/div/div[1]/div[1]/div/div').text
    
    try:
        data['ad_text'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[5]/div/p').text
    except: 
        data['ad_text'] = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[6]/div/p').text


    print(data['title'])

    atts = driver.find_elements(By.XPATH,'/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[4]/ul/li')

    for att in atts:
        try: 
            key  = att.find_element(By.XPATH, 'span[1]').text
            val  = att.find_element(By.XPATH, 'span[2]').text
        except: 
            key  = att.find_element(By.XPATH, 'span').text
            val  = att.find_element(By.XPATH, 'a').text
        print(key, val)
        data[key] = val

    return data 

def collect_ad(ad_number):
    main_url = 'https://www.unegui.mn/avto-mashin/-avtomashin-zarna/'

    driver = webdriver.Chrome()
    driver.get(main_url)

    driver.find_element(By.XPATH, f"/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[{ad_number}]/div[2]/a").click()
    data = collect_data(driver)

    return data

ad_list = range(45,61)

results = Parallel(n_jobs=4)(delayed(collect_ad)(n) for n in ad_list)
# Save to dataframe
df = pd.DataFrame(results)  
# Save to csv
df.to_csv('unegui/unegui_ads_4.csv', index=False, encoding='utf-8-sig') 