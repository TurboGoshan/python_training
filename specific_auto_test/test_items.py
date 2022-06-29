import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_presents(browser):
    browser.get(link)
    add_to_basket_button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert add_to_basket_button > 0, "button is not present"
    time.sleep(3)
