from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

driver = webdriver.Safari()

driver.get("https://www.google.com")

element = driver.find_element_by_class_name("gLFyf")

element.clear()
element.send_keys("sam")
element.send_keys(Keys.RETURN)




