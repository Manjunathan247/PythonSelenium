import logging

import pytest
from selenium import webdriver
from helpers.Read_Json_Helper import config_read, data_read


@pytest.fixture()
def driver_init(request):
    if config_read('browser').lower() == 'chrome':
        driver = webdriver.Chrome(config_read('chromedriver_path'))
    elif config_read('browser').lower() == 'firefox':
        driver = webdriver.firefox
    elif config_read('browser').lower() == 'chromeheadless':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(config_read('chromedriver_path'), chrome_options=chrome_options)
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(config_read('implicitwait'))
    driver.get(config_read('url'))
    actualTitle = driver.title
    assert actualTitle == data_read('practicepage_title')
    yield
    driver.close()

