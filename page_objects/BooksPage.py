from selenium import webdriver
from selenium.webdriver.common.by import By


class BooksPage:

    first_book_selector = "div.a-section.octopus-pc-card-content li"

    def __init__(self, driver ):
        self.driver = driver

    def SelectFirstBookNouveautes(self):
        self.driver.find_elements(By.CSS_SELECTOR, self.first_book_selector)[0].click()
