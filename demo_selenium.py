from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    chrome_options=chrome_options
)

i = 0
records = []
while True:
    driver.get(f"https://www.hktvmall.com/hktv/zh/search_a?keyword=%E6%B2%B9&page={i}")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-brief"))
    )

    cells = driver.find_elements_by_css_selector(".product-brief")

    for cell in cells:
        try:
            elem_title = cell.find_element_by_css_selector(".brand-product-name > h4")
            elem_price = cell.find_element_by_css_selector(".price")
            print(elem_title.text, elem_price.text)

            record = {
                "name": elem_title.text,
                "price": elem_price.text
            }

            records.append(record)
        except:
            pass

    next_btn = driver.find_element_by_css_selector("#paginationMenu_nextBtn")

    if next_btn.get_attribute("class") == "disabled":
        print("BREAK!")
        break

    if len(records) > 500:
        break

    i += 1

# records
driver.close()
