from page_objects.CartPage import CartPage
from page_objects.ConfirmationPage import ConfirmationPage
from page_objects.HomePage import HomePage
from page_objects.BooksPage import BooksPage

from selenium import webdriver

from page_objects.ProductPage import ProductPage


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
    bookspage=BooksPage(driver)
    bookspage.SelectFirstBookNouveautes()
    productpage = ProductPage(driver)
    productpage.addToCart()
    confirmationpage=ConfirmationPage(driver)
    confirmationpage.openCart()
    cartpage=CartPage(driver)
    cartpage.changeQuantity("2")
    cartpage.get_quantity()

    assert "2" == cartpage.get_quantity()
    driver.quit()




