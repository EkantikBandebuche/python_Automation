import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

@pytest.fixture(autouse=True)
def start_automatic_fixture():
    print('start test with automatic fixture')

# @pytest.fixture(scope='module')
@pytest.fixture(scope='function')
def setup_teardown():
    driver.get('https://boom.tv/')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign In').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'email').send_keys("ekantikb@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, 'password').send_keys("Ekantik0808")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="new_login_modal"]/div/div/div/form[1]/button').click()
    time.sleep(2)

    print("log In")
    yield
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign Out').click()
    print("logout")



@pytest.mark.usefixtures("setup_teardown")
def test1_apex():
    driver.find_element(By.XPATH, '//*[@class="landing_side_item"][1]').click()
    assert driver.title == "BOOM.TV -AVGL Weeklies Return featuring Fortnite and Apex Legends"
    print('test 1')
    driver.close()


@pytest.mark.usefixtures("setup_teardown")
def test1_apex2():
    driver.find_element(By.XPATH, '//*[@class="landing_side_item"][2]').click()
    assert driver.title == "BOOM.TV -Boom.tv Events"
    print('test 2')
    driver.close()


@pytest.mark.usefixtures("setup_teardown")
def test1_apex3():
    driver.find_element(By.XPATH, '//*[@class="landing_side_item"][3]').click()
    assert driver.title == "BOOM.TV -Boom.tv Events"
    print('test 3')
    driver.close()




