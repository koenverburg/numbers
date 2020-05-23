import os
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()

browser = webdriver.Firefox()
browser.get('https://github.com/login')

if browser.find_element_by_id('login_field'):
    loginElement = browser.find_element_by_id('login_field')
    loginElement.send_keys(os.environ['GITHUB_USERNAME'])

if browser.find_element_by_id('password'):
    passwordElement = browser.find_element_by_id('password')
    passwordElement.send_keys(os.environ['GITHUB_PASSWORD'])

    form = browser.find_element_by_xpath('/html/body/div[3]/main/div/form')
    form.submit()


browser.get(
    'https://github.com/{0}?tab=repositories'.format(os.environ['GITHUB_USERNAME']))

raw_repos = browser.find_elements_by_class_name('py-4')
print(raw_repos)
