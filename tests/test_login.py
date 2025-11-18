# tests/test_login.py
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

SCREENSHOT_DIR = "tests/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # remove this line if you want to see the browser
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(path)
    print("Saved screenshot:", path)

def test_login_valid_credentials(driver):
    # Replace the URL and selectors with your actual login page
    url = "https://example.com/login"
    driver.get(url)
    driver.find_element(By.NAME, "username").send_keys("valid_user")
    driver.find_element(By.NAME, "password").send_keys("valid_password")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait a moment then assert successful login (change selector as needed)
    time.sleep(1)
    assert "dashboard" in driver.current_url or driver.find_elements(By.ID, "logout")
    take_screenshot(driver, "valid_login_success")

def test_login_invalid_credentials(driver):
    url = "https://example.com/login"
    driver.get(url)
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("invalid_user")
    driver.find_element(By.NAME, "password").send_keys("wrong_pass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Check for an error message
    time.sleep(1)
    errors = driver.find_elements(By.CLASS_NAME, "error")
    take_screenshot(driver, "invalid_login_failure")
    assert len(errors) > 0 or "invalid" in driver.page_source.lower()
