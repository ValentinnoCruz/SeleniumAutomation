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
    """Capture a screenshot for both passed and failed tests."""
    outcome = yield
    report = outcome.get_result()
    driver = item.funcargs.get("driver", None)  # Access the driver fixture if available

    if driver:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        # Save a screenshot for every test
        screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
        driver.save_screenshot(screenshot_path)

        # Attach screenshot to pytest-html report
        pytest_html = item.config.pluginmanager.getplugin("html")
        if pytest_html:
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(screenshot_path))
            report.extra = extra