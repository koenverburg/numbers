import os
import time
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

browser = webdriver.Firefox()
browser.get("https://github.com/login")


def get_first(_value):
    return next(iter(_value))


def main():
    if browser.find_element_by_id("login_field"):
        loginElement = browser.find_element_by_id("login_field")
        loginElement.send_keys(os.environ["GITHUB_USERNAME"])
    if browser.find_element_by_id("password"):
        passwordElement = browser.find_element_by_id("password")
        passwordElement.send_keys(os.environ["GITHUB_PASSWORD"])

    form = browser.find_element_by_xpath("/html/body/div[3]/main/div/form")
    form.submit()

    time.sleep(3)

    whitelist = os.environ["WHITE_LISTED_REPOS"].split(",")
    readme = open("./readme.md", "a+")
    for repo in whitelist:
        netlify_stats_page = "https://github.com/{0}/{1}/actions?query=workflow%3A%22Netlify+Deploy%22".format(os.environ["GITHUB_USERNAME"], repo)
        browser.get(netlify_stats_page)
        branch = get_first(browser.find_elements_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/a")).text
        pipeline_duration = get_first(browser.find_elements_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/div[1]/details/summary/span")).text
        last_deployment_datetime = browser.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/span/time-ago").get_attribute("datetime")
        markdown_row = "| {0} | {1} | {2} | {3} |\n".format(repo, branch, pipeline_duration, last_deployment_datetime)
        readme.write(markdown_row)
        print(markdown_row)
        # print(repo)
        # print(branch)
        # print(pipeline_duration)
        # print(last_deployment_datetime)
        continue
    readme.close()


if __name__ == "__main__":
    main()
