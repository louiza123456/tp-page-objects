from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPage:

    addToCart_selector = "input[name='submit.add-to-cart']"

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.addToCart_selector).click()
