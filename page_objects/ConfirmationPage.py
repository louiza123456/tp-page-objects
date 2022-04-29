from selenium import webdriver
from selenium.webdriver.common.by import By


class ConfirmationPage:
    openCart_selector = "#sw-gtc>span>a"



    def __init__(self, driver ):
        self.driver = driver

    def openCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.openCart_selector).click()
