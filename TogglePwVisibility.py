import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPasswordToggle:

    def test_password_initially_hidden(self, driver):
        """Test if the password field is initially hidden (masked)"""

        driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")
        wait = WebDriverWait(driver, 10)

        password_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
        assert password_input.get_attribute("type") == "password", "Password should initially be hidden"
        password_input.send_keys("Canon1234")  # Ensure password is entered
        

        screenshot_path = "screenshots/password_initially_hidden.png"
        driver.save_screenshot(screenshot_path)
        print(f"✅ Screenshot saved: {screenshot_path}")

    def test_toggle_password_visible(self, driver):
        """Test toggling the password field to visible"""

        driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")
        wait = WebDriverWait(driver, 10)

        password_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
        password_input.send_keys("Canon1234")  # Ensure password is entered

        toggle_button = driver.find_element(By.XPATH, "//label[@for='show-pw']")
        
        # Click toggle button
        toggle_button.click()
        time.sleep(1)  # Allow UI to update

        # Verify password is now visible
        assert password_input.get_attribute("type") == "text", "Password should be visible after toggle"

        screenshot_path = "screenshots/password_visible.png"
        driver.save_screenshot(screenshot_path)
        print(f"✅ Screenshot saved: {screenshot_path}")

    def test_toggle_password_hidden_again(self, driver):
        """Test toggling the password field back to hidden"""

        driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")
        wait = WebDriverWait(driver, 10)

        password_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
        password_input.send_keys("Canon1234")  # Ensure password is entered

        toggle_button = driver.find_element(By.XPATH, "//label[@for='show-pw']")

        # Click to show password first
        toggle_button.click()
        time.sleep(1)

        # Click again to hide the password
        toggle_button.click()
        time.sleep(1)

        # Verify password is now hidden again
        assert password_input.get_attribute("type") == "password", "Password should be hidden after toggling back"

        screenshot_path = "screenshots/password_hidden_again.png"
        driver.save_screenshot(screenshot_path)
        print(f"✅ Screenshot saved: {screenshot_path}")



# ----------------- Test Case -----------------

# import pytest
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class TestShowPW:
#     def test_show_password_toggle(self, driver):
#         """Test if toggling the eye icon correctly reveals/hides the password"""

#         # Open the login page
#         driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")

#         # Wait for page to load
#         wait = WebDriverWait(driver, 10)

#         # Input Email
#         email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
#         email_input.send_keys("QAStandard4@canon.com")

#         # Input Password
#         password_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
#         password_input.send_keys("Canon1234")

#         # Ensure the initial input type is 'password'
#         assert password_input.get_attribute("type") == "password", "Password field should initially be hidden"
#         print("✅ Password field is initially hidden.")

#         # Click the show password eye
#         toggle_button = driver.find_element(By.XPATH, "//label[@for='show-pw']")
#         toggle_button.click()
#         time.sleep(1)  # Give UI time to reflect change

#         # Verify the password input type changed to 'text'
#         assert password_input.get_attribute("type") == "text", "Password should be visible after clicking the toggle"
#         print("✅ Password is now visible.")

#         # Click again to hide the password
#         toggle_button.click()
#         time.sleep(1)

#         # Verify it changed back to 'password'
#         assert password_input.get_attribute("type") == "password", "Password should be hidden after clicking toggle again"
#         print("✅ Password is hidden again after second toggle.")

#         print("🎉 Test Passed: Password visibility toggle works correctly!")
