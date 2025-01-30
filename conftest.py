


# ----------------- ---------------- -----------------
# ----------------- Screenshot working -----------------
# # ----------------- ---------------- -----------------
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """Fixture to initialize and quit WebDriver."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver  # Pass the driver to the test
    driver.quit()  # Close the browser after the test

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot and attach it to the HTML report."""
    outcome = yield
    report = outcome.get_result()
    driver = item.funcargs.get("driver", None)  # Access the driver from the test function

    # Take a screenshot if the driver is available
    if report.when == "call" and driver:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        # Save the screenshot with the test name
        screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
        driver.save_screenshot(screenshot_path)

        # Attach screenshot to the pytest-html report
        pytest_html = item.config.pluginmanager.getplugin("html")
        if pytest_html:
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(screenshot_path, mime_type="image/png"))
            report.extra = extra