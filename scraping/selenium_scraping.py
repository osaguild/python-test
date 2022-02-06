from selenium import webdriver
import time

chrome = webdriver.Chrome(executable_path='./chrome/chromedriver')

try:
    chrome.get('https://saitama-premium-search.com/')
    time.sleep(2)
    values = chrome.find_elements_by_class_name('content.title')
    for value in values:
        print(value.text)
finally:
    chrome.quit()

