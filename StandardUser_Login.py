import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserLogin:
    def test_User_Login(self, driver):
        # Open the login page
        driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")

        # Wait for page to load
        wait = WebDriverWait(driver, 10)

        email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_input.send_keys("QAStandard4@canon.com")

        PW_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
        PW_input.send_keys("Canon1234")

        # Click login button
        driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']").click()

        # Check successful login
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='user-role']"))
            )
            print("User logged in successfully")
        except Exception as e:
            pytest.fail("User login failed")

        time.sleep(2)  # or do some more checks
