import requests
from time import time
import time

class Login():

    def __init__(self, driver):
        self.driver = driver


    def login(self):
        links = self.driver.find_elements_by_css_selector("a")
        try:


            Login_link = self.driver.find_element_by_xpath("//a[contains(text(),'Login')]")
            Login_link.click()
            time.sleep(3)

            Email = self.driver.find_element_by_id("email")
            Email.send_keys("hello@atg.world")
            time.sleep(2)
            Password = self.driver.find_element_by_id("password")
            Password.send_keys("Pass@123")

            Sign_in = self.driver.find_element_by_xpath("//button[@type='submit']")
            Sign_in.click()
            time.sleep(3)
        except Exception as e:
            print(e)
        for link in links:
            r = requests.head(link.get_attribute('href'))
            print(r.status_code == 200)



    def post_article(self,url):
        try:

            Dropdown = self.driver.find_element_by_xpath("//button[@id='dropdownMenuButton']")
            Dropdown.click()
            time.sleep(2)

            Article = self.driver.find_element_by_xpath("//a[contains(text(),'Article')]")
            Article.click()
            time.sleep(3)

            content = self.driver.pagesource
            time.sleep(3)
            title = self.driver.find_element_by_xpath("//input[@id='title']")
            title.send_keys("New post")
            time.sleep(3)

            Desc = self.driver.find_element_by_xpath("//div[@class='fr-element fr-view']")
            Desc.send_keys("Hello everyone this post written using python and selenium!")

            Post = self.driver.find_element_by_xpath("//button[contains(text(),'Post')]")
            Post.click()
        except Exception as e:
            print(e)

    def HTTPresp(self,url):
        r = requests.get(url)
        print("status code of :" +url)
        print(r.status_code )

    def broken_links(self,url):
        self.driver.get(url)
        links = self.driver.find_elements_by_css_selector("a")
        images = self.driver.find_elements_by_css_selector("img")
        for link in links:
            r = requests.head(link.get_attribute('href'))
            print(r.status_code == 200)