import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.mozilla.org"
title = "Internet for people"

@pytest.fixture


def webFix():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        element = wait(driver,10).until(EC.title_contains(title))
        print('waited on browser')
    except Exception as ex:
        print('Something went wrong')
        print(ex)
    yield driver  
    
    #always quick driver
    driver.quit()
    
    
def test_web_link(webFix):
    webFix.find_element_by_link_text("Learn more").click()
    title = webFix.title
    assert "Firefox" in title
    
def test_web_links(webFix):
    links = webFix.find_elements_by_tag_name("a")
    for link in links:
        href = link.get_attribute("href")
        assert 'cnbc.com' in href or 'bbc.com' in href or 'mozilla' in href \
        or 'firefox' in href or 'buzzfeed' in href or 'getpocket' in href 


def test_accounts_form(webFix):
    webFix.find_element_by_link_text("Get a Firefox account").click()
    try:
      #print("Opened firefox account link")
      element = wait(webFix,3).until(EC.presence_of_element_located(By.CLASS_NAME, 'email tooltip-below'))
           
    except Exception as ex:
      #print('An exception occurred')
      print(ex)
    text_input = webFix.find_element_by_tag_name('input')
    text_input.sendkeys('triniseanf@gmail.com')
    webFix.find_element_by_id('submit-btn').click()
    prefilledEmail = 'none'
    try:
        prefilledEmail = wait(webFix, 3).until(EC.presence_of_element_located(By.CLASS_NAME, 'prefillEmail'))
        print(prefilledEmail)
    except Exception as ex:
        print('An exception occurred')
        print(ex)
    assert 'triniseanf@gmail.com' in prefilledEmail.text 