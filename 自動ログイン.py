from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get("https://slack.com/intl/ja-jp/get-started#/createnew")
browser.find_element(By.ID,"google_login_button").click()
browser.find_element(By.ID,"identifierId").send_keys("takuseki1223@gmail.com")
browser.find_element(By.CLASS_NAME,"VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b").click()