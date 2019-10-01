from selenium import webdriver
import requests
import time
from screnshot.test2 import Login
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
d= DesiredCapabilities.CHROME
d['logging pref'] = {'browser':'ALL'}

driver = webdriver.Chrome("E:\Tester\selenium\chromedriver.exe",desired_capabilities=d)
url ="https://www.atg.party"
url2 = "https://www.atg.party/article"
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)

r = requests.get(url)
print (r.status_code)

for entry in driver.get_log('browser'):
    if entry['level'] =="SEVERE":
        print("some resources sre unloaded " ,entry["message"])

    if entry["level"] == "WARNING":
        print('java script DOM Error  ',entry["message"])

'''def Login_case():
    Log = Login(driver)
    Log.login()
    Log.HTTPresp(url)
    driver.quit()
def article():
    
    article = Login(driver)
    article.post_article(url2)
    article.HTTPresp(url2)'''

links = driver.find_elements_by_css_selector("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(r.status_code == 200)
Login_link = driver.find_element_by_xpath("//a[contains(text(),'Login')]")
Login_link.click()
time.sleep(3)

Email = driver.find_element_by_id("email")
Email.send_keys("hello@atg.world")
time.sleep(2)
Password = driver.find_element_by_id("password")
Password.send_keys("Pass@123")

Sign_in = driver.find_element_by_xpath("//button[@type='submit']")
Sign_in.click()
time.sleep(3)


driver.quit()
