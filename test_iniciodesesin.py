# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestIniciodesesin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_iniciodesesin(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.ID, "login2").click()
    self.driver.find_element(By.ID, "loginusername").click()
    self.driver.find_element(By.ID, "loginusername").send_keys("alejandro.10218@gmail.com")
    self.driver.find_element(By.ID, "loginpassword").send_keys("123456789")
    self.driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-primary").click()
    self.driver.find_element(By.ID, "logInModal").click()
    self.driver.find_element(By.ID, "login2").click()
    self.driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-secondary").click()
  
