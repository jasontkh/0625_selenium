# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# # s = Service(ChromeDriverManager().install())
# # s.path
#
# import undetected_chromedriver.v2 as uc
# driver = uc.Chrome(service=Service(ChromeDriverManager().install()))
# # driver = uc.Chrome(browser_executable_path=s.path)
# driver.get('https://nowsecure.nl')
import time
print("__name__", __name__)
if __name__ == '__main__':
    print("b")
    import undetected_chromedriver as uc

    driver = uc.Chrome()
    driver.get('https://nowsecure.nl')

    time.sleep(1000000)
