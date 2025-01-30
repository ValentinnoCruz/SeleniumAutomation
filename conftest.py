import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserLogin:
    def test_User_Login(self, driver):  # Use the `driver` fixture
        driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")
        wait = WebDriverWait(driver, 10)

        # Input email and password
        wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("QAStandard4@canon.com")
        wait.until(EC.presence_of_element_located((By.ID, "current-password"))).send_keys("Canon1234")

        # Click SIGN IN
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='SIGN IN']"))).click()

        # Wait for dashboard and verify login
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-role")))
            print("User logged in successfully")
        except Exception as e:
            driver.save_screenshot("screenshots/login_failed.png")  # Capture failure screenshot
            assert False, f"User login failed: {str(e)}"













# import pytest

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Capture a screenshot on test failure."""
#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("driver")
#         if driver:
#             screenshot_path = f"screenshots/{item.name}.png"
#             driver.save_screenshot(screenshot_path)
#             pytest_html = item.config.pluginmanager.getplugin("html")
#             if pytest_html:
#                 extra = getattr(report, "extra", [])
#                 extra.append(pytest_html.extras.image(screenshot_path))
#                 report.extra = extra
