

# ------ Currently working ------

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_password_toggle(driver, request):
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
    print(f"✅ Password initially Hidden: {screenshot1}")

    # Step 2: Click toggle to show password
    toggle_button.click()
    time.sleep(1)  # Allow UI to update
    assert password_input.get_attribute("type") == "text", "Password should be visible after toggle"
    screenshot2 = "screenshots/password_visible.png"
    driver.save_screenshot(screenshot2)
    request.node.screenshot_paths.append(screenshot2)  # Store screenshot path
    print(f"✅ Password visible after toggle: {screenshot2}")

    # Step 3: Click toggle again to hide password
    toggle_button.click()
    time.sleep(1)
    assert password_input.get_attribute("type") == "password", "Password should be hidden after toggling back"
    screenshot3 = "screenshots/password_hidden_again.png"
    driver.save_screenshot(screenshot3)
    request.node.screenshot_paths.append(screenshot3)  # Store screenshot path
    print(f"✅ Password hidden after toggle: {screenshot3}")

    print("🎉 Test Passed: Password visibility toggle works correctly!")




# ------------------ Working 3 tests ------------------

# import pytest
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class TestPasswordToggle:

#     def test_password_initially_hidden(self, driver):
#         """Test if the password field is initially hidden (masked)"""

#         driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")
#         wait = WebDriverWait(driver, 10)

#         password_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
#         assert password_input.get_attribute("type") == "password", "Password should initially be hidden"
#         password_input.send_keys("Canon1234")  # Ensure password is entered
        

#         screenshot_path = "screenshots/password_initially_hidden.png"
#         driver.save_screenshot(screenshot_path)
#         print(f"✅ Screenshot saved: {screenshot_path}")

#     def test_toggle_password_visible(self, driver):
#         """Test toggling the password field to visible"""

#         driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")
#         wait = WebDriverWait(driver, 10)

#         password_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
#         password_input.send_keys("Canon1234")  # Ensure password is entered

#         toggle_button = driver.find_element(By.XPATH, "//label[@for='show-pw']")
        
#         # Click toggle button
#         toggle_button.click()
#         time.sleep(1)  # Allow UI to update

#         # Verify password is now visible
#         assert password_input.get_attribute("type") == "text", "Password should be visible after toggle"

#         screenshot_path = "screenshots/password_visible.png"
#         driver.save_screenshot(screenshot_path)
#         print(f"✅ Screenshot saved: {screenshot_path}")

#     def test_toggle_password_hidden_again(self, driver):
#         """Test toggling the password field back to hidden"""

#         driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")
#         wait = WebDriverWait(driver, 10)

#         password_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
#         password_input.send_keys("Canon1234")  # Ensure password is entered

#         toggle_button = driver.find_element(By.XPATH, "//label[@for='show-pw']")

#         # Click to show password first
#         toggle_button.click()
#         time.sleep(1)

#         # Click again to hide the password
#         toggle_button.click()
#         time.sleep(1)

#         # Verify password is now hidden again
#         assert password_input.get_attribute("type") == "password", "Password should be hidden after toggling back"

#         screenshot_path = "screenshots/password_hidden_again.png"
#         driver.save_screenshot(screenshot_path)
#         print(f"✅ Screenshot saved: {screenshot_path}")



# ----------------- Original 1 test -----------------

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
