
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserLogin:
    def test_User_Login(self, driver, request):
        """Test successful user login and capture screenshot."""

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

        # Initialize screenshot storage
        request.node.screenshot_paths = []

        # Check successful login
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='user-role']"))
            )
            print("✅ User logged in successfully.")

            # Capture screenshot after successful login
            screenshot_path = "screenshots/user_login_success.png"
            driver.save_screenshot(screenshot_path)
            request.node.screenshot_paths.append(screenshot_path)  # Store screenshot path

        except Exception as e:
            pytest.fail("❌ User login failed.")

        time.sleep(2)  # Optional delay for UI checks

class TestPasswordToggle:
    def test_password_toggle(self, driver, request):
        """Test password toggle functionality in a single test while capturing multiple screenshots."""

        driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")
        wait = WebDriverWait(driver, 10)

        password_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
        password_input.send_keys("Canon1234")  # Ensure password is entered

        toggle_button = driver.find_element(By.XPATH, "//label[@for='show-pw']")

        # Initialize screenshot storage
        request.node.screenshot_paths = []

        # Step 1: Verify password is initially hidden
        assert password_input.get_attribute("type") == "password", "Password should initially be hidden"
        screenshot1 = "screenshots/password_initially_hidden.png"
        driver.save_screenshot(screenshot1)
        request.node.screenshot_paths.append(screenshot1)  # Store screenshot path
        print(f"✅ Screenshot saved: {screenshot1}")

        # Step 2: Click toggle to show password
        toggle_button.click()
        time.sleep(1)  # Allow UI to update
        assert password_input.get_attribute("type") == "text", "Password should be visible after toggle"
        screenshot2 = "screenshots/password_visible.png"
        driver.save_screenshot(screenshot2)
        request.node.screenshot_paths.append(screenshot2)  # Store screenshot path
        print(f"✅ Screenshot saved: {screenshot2}")

        # Step 3: Click toggle again to hide password
        toggle_button.click()
        time.sleep(1)
        assert password_input.get_attribute("type") == "password", "Password should be hidden after toggling back"
        screenshot3 = "screenshots/password_hidden_again.png"
        driver.save_screenshot(screenshot3)
        request.node.screenshot_paths.append(screenshot3)  # Store screenshot path
        print(f"✅ Screenshot saved: {screenshot3}")

        print("🎉 Test Passed: Password visibility toggle works correctly!")



# ------- old working with original conftest.py -------

# import time
# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class TestUserLogin:
#     def test_User_Login(self, driver):
#         # Open the login page
#         driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")

#         # Wait for page to load
#         wait = WebDriverWait(driver, 10)

#         email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
#         email_input.send_keys("QAStandard4@canon.com")

#         PW_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
#         PW_input.send_keys("Canon1234")

#         # Click login button
#         driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']").click()

#         # Check successful login
#         try:
#             WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.XPATH, "//div[@class='user-role']"))
#             )
#             print("User logged in successfully")
#         except Exception as e:
#             pytest.fail("User login failed")

#         time.sleep(2)  # or do some more checks
