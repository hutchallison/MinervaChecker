from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

loginPage = "https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin"

driver = webdriver.Chrome()

driver.get(loginPage)

sleep(3)