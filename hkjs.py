from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://bet.hkjc.com/football/index.aspx?lang=ch"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)

rows = driver.find_elements(By.CSS_SELECTOR, ".couponTable > .couponRow")
all_records = []
for i, row in enumerate(rows):
    try:
        name = row.find_element(By.CSS_SELECTOR, ".cteams").text
        print([name])
    except:
        pass

    # all_records.append([name, win_rate])
    # break
