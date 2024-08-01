import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://boom.tv/")
driver.implicitly_wait(10)
time.sleep(2)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT,'Sign In').click()
time.sleep(2)
driver.find_element(By.NAME,'email').send_keys("ekantikb@gmail.com")
time.sleep(2)
driver.find_element(By.NAME,'password').send_keys("Ekantik0808")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="new_login_modal"]/div/div/div/form[1]/button').click()
time.sleep(2)
print(driver.title)

assert driver.title == "BOOM.TV -LIVE"
print("successful login")
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,'Sign Out' ).click()
print("logout")

