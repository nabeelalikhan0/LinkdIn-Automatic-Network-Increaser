from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as p
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/mynetwork/grow/")


email = "nabeel03103n@gmail.com"
password = "qd5EuU7WX_@y0jt"


input_email = driver.find_element(By.ID, "username")
input_password = driver.find_element(By.ID, "password")

input_email.send_keys(email)
input_password.send_keys(password)
input_password.send_keys(Keys.RETURN)


load_more_btn = driver.find_element(By.XPATH, "//*[text()='Load more']")
driver.execute_script("arguments[0].click();", load_more_btn)


connect_btns = driver.find_elements(By.XPATH, "//*[text()='Connect']")


for connect_btn in connect_btns:
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", connect_btn)
        sleep(0.5)  # allow any animations to settle
        driver.execute_script("arguments[0].click();", connect_btn)
        sleep(1)  # wait between clicks
    except Exception as e:
        print(f"Skipping button due to error: {e}")