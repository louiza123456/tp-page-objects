import keyword

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class CartPage:
    quantity_select_selector ="select[name='quantity']"
    get_quantity_selector = "2"



    def __init__(self, driver):
        self.driver = driver

    def changeQuantity(self, quantity):
       menu_deroulant= Select(self.driver.find_element(By.CSS_SELECTOR, self.quantity_select_selector))
       menu_deroulant.select_by_visible_text(quantity)

    def get_quantity(self):
        return Select(self.driver.find_element(By.CSS_SELECTOR, self.quantity_select_selector)).first_selected_option.text


