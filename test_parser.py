from selenium import webdriver
import conftest
import time

#link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    time.sleep(1)
    browser_text=browser
    print(browser,'$$$$$')
    link = f"http://selenium1py.pythonanywhere.com/{browser}/catalogue/coders-at-work_207/"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(6)
    #  //*[@id="add_to_basket_form"]/button
    #browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    rest_text=browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    bit_text=rest_text.text
    print(bit_text,' <:-)',browser_text)
    assert rest_text==rest_text
    browser.find_element_by_css_selector("#login_link")
    browser.quit()
## pytest -s -v --language=ru test_parser.py
#   pytest -s -v --language=de test_parser.py

