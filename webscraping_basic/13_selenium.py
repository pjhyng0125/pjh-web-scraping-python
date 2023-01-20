from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# browser = webdriver.Chrome("C:/pjh/util/chromedriver_win32/chromedriver.exe")

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

browser.get("http://naver.com")

while(True):
    pass

# ele = browser.find_element_by_class_name("link_login")
# elem = browser.find_element_by_id("query")
# elem = browser.find_elements_by_tag_name("a")

# from seleninum.webdriver.common.keys import Keys
# elem = browser.send_keys("가즈아아")
# elem = browser.send_keys(Keys.ENTER)

# browser.quit()