# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.action_chains import ActionChains
#
# @pytest.fixture
# def setup():
#     driver = webdriver.chrome()
#     url = "https://demoqa.com/slider"
#     driver.get(url)
#     yield driver
#     driver.quit()
#
# def test_slider(setup):
#     actions = ActionChains(setup)
#     slider = setup.find_element(By.ID, "slider")
#     time.sleep(2)
#     actions.drag_and_drop_by_offset(slider,60,80).perform()

import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def setup():

    driver = webdriver.Chrome()

    url = "https://demoqa.com/slider"
    driver.get(url)

    yield driver

    driver.quit()


def test_slider(setup):

    actions = ActionChains(setup)

    slider = setup.find_element(By.ID, "slider")

    time.sleep(2)

    actions.drag_and_drop_by_offset(slider, 60, 0).perform()