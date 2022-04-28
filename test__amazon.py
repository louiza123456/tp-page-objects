from page_objects.HomePage import HomePage
from page_objects.BooksPage import BooksPage

from selenium import webdriver


def test_amazon1():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr")
    driver.maximize_window()
    driver.quit()

def test_page_object():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr")
    homePage = HomePage(driver)
    homePage.closecookiepopup()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()

