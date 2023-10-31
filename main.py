import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from decouple import config

# Retrive Global Variables from .env file

PHONE_NUMBER = config('PHONE_NUMBER')
EMAIL = config('EMAIL')
CNP_H = config('CNP_H')
NAME_H = config('NAME_H')
PRENUME_H = config('PRENUME_H')
ADRESA_H = config('ADRESA_H')

CNP_W = config('CNP_W')
NAME_W = config('NAME_W')
PRENUME_W = config('PRENUME_W')
COUNTY_W =  config('COUNTY_W')
TOWN_VILLAGE_W = config('TOWN_VILLAGE_W')
ADRESA_W = config('ADRESA_W')



# Driver
driver = webdriver.Firefox()
driver.maximize_window()

# URL

driver.get("https://casatorii.primarie3.ro/Programare.aspx")

## Start Input
# Date Selector
TARGET_DATE_TEXT = '17'

time.sleep(1)

date_element = driver.find_element(By.LINK_TEXT, TARGET_DATE_TEXT)
date_element.click()

# Hour Selector

TARGET_HOUR_TEXT = '11:30' # write what hour you need
TARGET_HOUR_TEXT = '11:45' # write what hour you need
hour_element = driver.find_element(By.XPATH, f"//td[text()='{TARGET_HOUR_TEXT}']")
hour_element.click()

# Phone Input
phone_input = driver.find_element(By.ID, 'ctl00_ContentHolder_Phone')
phone_input.send_keys(PHONE_NUMBER)

# Email Input
email_input = driver.find_element(By.ID, 'ctl00_ContentHolder_Email')
email_input.send_keys(EMAIL)

## Click 'Pasul Urmator'

next_button = driver.find_element(By.ID, 'ctl00_ContentHolder_Tab0_NextButton')
next_button.click()

## HUSBAND DATES

# CNP
cnp_h_input = driver.find_element(By.ID, 'ctl00_ContentHolder_H_CNP')
cnp_h_input.send_keys(CNP_H)

# Name
name_h_input = driver.find_element(By.ID, 'ctl00_ContentHolder_H_Firstname')
name_h_input.send_keys(NAME_H)

# Prenume
prenume_h_input = driver.find_element(By.ID, 'ctl00_ContentHolder_H_Lastname')
prenume_h_input.send_keys(PRENUME_H)

# Adresa
adresa_h_input = driver.find_element(By.ID, 'ctl00_ContentHolder_H_Home')
adresa_h_input.send_keys(ADRESA_H)

## Click 'Pasul Urmator'
next_button = driver.find_element(By.ID, 'ctl00_ContentHolder_Tab1_NextButton')
next_button.click()

## WIFE DATES

# CNP
cnp_w_input = driver.find_element(By.ID, 'ctl00_ContentHolder_W_CNP')
cnp_w_input.send_keys(CNP_H)

# Name
name_w_input = driver.find_element(By.ID, 'ctl00_ContentHolder_W_Firstname')
name_w_input.send_keys(NAME_W)

# Prenume
prenume_w_input = driver.find_element(By.ID, 'ctl00_ContentHolder_W_Lastname')
prenume_w_input.send_keys(PRENUME_W)

# County
county_dropdown_w = driver.find_element(By.ID, 'ctl00_ContentHolder_W_County')
county_selector = Select(county_dropdown_w)
county_selector.select_by_value(COUNTY_W)

# Town/Village
town_village_w = driver.find_element(By.ID, 'ctl00_ContentHolder_W_Locality')
town_village_w_selector = Select(town_village_w)
town_village_w_selector.select_by_value(TOWN_VILLAGE_W)

# Adresa

adresa_w_input = driver.find_element(By.ID, 'ctl00_ContentHolder_W_Home')
adresa_w_input.send_keys(ADRESA_W)

# Click Consent
consent_input = driver.find_element(By.ID,'ctl00_ContentHolder_Check_Terms')
consent_input.click()

## END



