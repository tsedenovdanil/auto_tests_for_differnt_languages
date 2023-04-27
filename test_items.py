from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_guest_should_see_login_link(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR,".btn-add-to-basket"), "Basket not found"
    time.sleep(10)
