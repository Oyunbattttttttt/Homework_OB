from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np



search_data_main_path = '4.lms_system/'
df = pd.read_excel(search_data_main_path + 'dataframe_v3.xlsx', engine='openpyxl')

def collect_ad_details(driver):
    data = {}

    #Collect data
    try:
        data['Agent_1'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[3]/div[2]/app-agent-inquiry/div/div[2]/div[1]/div[1]/div[1]/div[2]/strong').text
    except:
        try:
            data['Agent_1'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[4]/div[2]/app-agent-inquiry/div/div[2]/div/div[1]/div[1]/div[2]/strong').text
        except:
            data['Agent_1'] = None 
    try:
        data['Agent_2'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[3]/div[2]/app-agent-inquiry/div/div[2]/div[2]/div[1]/div[1]/div[2]/strong').text
    except:
        try:
            data['Agent_2'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[4]/div[2]/app-agent-inquiry/div/div[2]/div[2]/div[1]/div[1]/div[2]/strong').text
        except:
            data['Agent_2'] = None

    try:    
        data['Agent_3'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[3]/div[2]/app-agent-inquiry/div/div[2]/div[3]/div[1]/div[1]/div[2]/strong').text
    except:
        try:
            data['Agent_3'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[4]/div[2]/app-agent-inquiry/div/div[2]/div[3]/div[1]/div[1]/div[2]/strong').text
        except:
            data['Agent_3'] = None
    
    try:
        data['Agent_4'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[3]/div[2]/app-agent-inquiry/div/div[2]/div[4]/div[1]/div[1]/div[2]/strong').text
    except:
        try:
            data['Agent_4'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[4]/div[2]/app-agent-inquiry/div/div[2]/div[4]/div[1]/div[1]/div[2]/strong').text
        except:    
            data['Agent_4'] = None
    
    try:
        data['Agent_5'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[3]/div[2]/app-agent-inquiry/div/div[2]/div[5]/div[1]/div[1]/div[2]/strong').text
    except:
        try:
            data['Agent_5'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[4]/div[2]/app-agent-inquiry/div/div[2]/div[5]/div[1]/div[1]/div[2]/strong').text
        except:    
            data['Agent_5'] = None

    
    try:
        data['start'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[3]/div[2]/app-agent-inquiry/div/div[1]/div[2]/div/div/div[1]/div[1]').text
    except:
        try:
            data['start'] = driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[4]/div[2]/app-agent-inquiry/div/div[1]/div[2]/div/div/div[1]/div[1]').text
        except:
            data['start'] = None



    return data


# Replace with your credentials
email_text = "oyunbat@mlw.mn"
password_text = "oyunbat@mlw.mn"
company_name = "ML Worldwide LLC"

# Setup Chrome driver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# Open the login page
driver.get("https://lms.mlholding.mn/login")

# Wait until page loads
wait = WebDriverWait(driver, 20)

# === Step 1: Click the company dropdown ===
company_dropdown = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[1]/div/div[2]/form/div/div[2]/mat-form-field/div[1]/div[2]/div/mat-select")
))
company_dropdown.click()

# === Step 2: Wait and click the desired company option ===
company_option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//mat-option//span[contains(text(), 'ML Worldwide LLC')]")
))
company_option.click()

# --- Step 2: Enter email ---
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[1]/div/div[2]/form/div/div[3]/mat-form-field/div[1]/div[2]/div/input")))
email_input.send_keys(email_text)

# --- Step 3: Enter password ---
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[1]/div/div[2]/form/div/div[4]/mat-form-field/div[1]/div[2]/div/input")))
password_input.send_keys(password_text)

# --- Step 4: Click login button ---
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()

# Done
print("✅ Login attempted.")

# Wait until the search input is visible
search_input = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-main-layout/div/div[2]/app-navbar/nav/div[2]/div[1]/app-operation-bar/div/div/div/div/input[1]"))
)

# Clear and input the search number
datalist = []

for ad_number in df['ad_number']:
    # Wait for and clear the search input
    search_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-main-layout/div/div[2]/app-navbar/nav/div[2]/div[1]/app-operation-bar/div/div/div/div/input[1]"))
    )
    search_input.clear()
    search_input.send_keys(str(ad_number))
    search_input.send_keys(Keys.ENTER)

    # Click the Inquiry button
    try:
        inquiry_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/nav/ul/li[2]/button"))
        )
        inquiry_button.click()
    except TimeoutException:
        print("⚠️ Agents button not found — skipping this ad.")

    # Click the Agents button
    try:
        agents_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[4]/div[2]/app-agent-inquiry/div/div[1]/div[2]/div/div"))
        )
        agents_button.click()
        
    except:
        try:
            agents_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[3]/div[2]/app-agent-inquiry/div/div[1]/div[2]/div/div"))
            )
            agents_button.click()
        except:
            try:
                agents_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main-layout/div/div[2]/div[1]/div/div/app-freight-operation/div/mat-sidenav-container/mat-sidenav-content/div[3]/div[2]/app-agent-inquiry/div/div[1]/div[3]/div/div"))
                )
                agents_button.click()
            except TimeoutException:
                print("⚠️ Agents button not found — skipping this ad.")

           
    # Collect the data and append to list
    data = collect_ad_details(driver)
    data['ad_number'] = ad_number  # add reference back to ad_number
    datalist.append(data)

    # Navigate back
    driver.back()



df = pd.DataFrame(datalist)
df[['Agent_1', 'Agent_2', 'Agent_3', 'Agent_4', 'Agent_5']].replace(['', np.nan], 'n,a')

df.to_excel('unegui_ads.xlsx', index=False)
