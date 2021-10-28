from selenium import webdriver
import conftest
import time


# link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_The_presence_of_a_button(browser1):
    time.sleep(1)
    browser_text = browser1
    print(browser_text, '$$$$$')

    link = f" http://selenium1py.pythonanywhere.com/{browser_text}/catalogue/coders-at-work_207/"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)

    #  //*[@id="add_to_basket_form"]/button
    # browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    def check_click(browser):
        try:
            rest_text = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]//buttton')
            bit_text = rest_text.text
            print(bit_text, ' <==(',browser_text,')')
        except :
            print( '<<    Keine button,Missing_button_Error   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            browser.quit()
    check_click(browser)
    # browser.find_element_by_css_selector("#login_link")

    browser.quit()
## pytest -s -v --language=ru test_parser.py
#   pytest -s -v --language=de test_parser.py
