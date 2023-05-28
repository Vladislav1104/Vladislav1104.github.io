from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
def main(input):
    driver = webdriver.Chrome()
    driver.get("https://htmlbase.ru/")
    a = driver.find_element(By.NAME, 'q')
    a.send_keys(input)
    a.send_keys(Keys.ENTER)
    time.sleep(60)