from ast import Assert
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\Servdoc\Downloads\chromedriver.exe")
driver.get("https://testlink.org/")

titlePage = driver.title

titleToConfirm = "TestLink"

assert titlePage == titleToConfirm
print("This page is TestLink!")

linkGitHub = driver.find_element("link text", "Access Git Repository (GitHub)")
linkGitHub.click()

titlePageGitHub = driver.title

assert "TestLink" in titlePageGitHub
print("This GitHub page has any relation with TestLink.")

# searchGitHub = driver.find_element("q").send_keys("jjoaox")
# searchGitHub = driver.find_element("q").send_keys(Keys.RETURN)