import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://boom.tv/")
driver.implicitly_wait(10)
time.sleep(2)
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT,'Sign In').click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,'Sign Up').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="new_login_modal"]/div/div/div/form[2]/input[4]').send_keys("ekantikqa")

driver.find_element(By.XPATH,'//*[@id="new_login_modal"]/div/div/div/form[2]/input[5]').send_keys("ekantik.qa@gmail.com")

driver.find_element(By.XPATH,'//*[@id="admin_login_password"]').send_keys("Ekantik0809")

driver.find_element(By.XPATH,'//*[@id="admin_login_password_confirmation"]').send_keys("Ekantik0809")

driver.find_element(By.XPATH,'//*[@id="admin_login_register_btn"]').click()
time.sleep(3)
print(driver.title)
assert driver.title == "BOOM.TV -LIVE"
