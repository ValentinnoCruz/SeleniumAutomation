import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pathlib import Path

# Global driver reference
driver = None

# Define base directory for reports & screenshots
REPORT_DIR = Path("Reports", datetime.now().strftime("%Y%m%d_%H%M%S"))
SCREENSHOT_DIR = REPORT_DIR / "screenshots"

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    global driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    request.cls.driver = driver  # Make driver available to test classes
    yield
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    
    if report.when in ['call', 'setup']:
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Create screenshot directory if needed
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
            
            # Capture screenshot
            screenshot_path = SCREENSHOT_DIR / f"{report.nodeid.replace('::', '_')}.png"
            driver.save_screenshot(str(screenshot_path))
            
            # Embed in report
            if pytest_html:
                # Use relative path for HTML report compatibility
                relative_path = os.path.relpath(
                    screenshot_path, 
                    start=REPORT_DIR
                )
                extra.append(pytest_html.extras.image(relative_path))
                
        report.extra = extra

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Set up the report directory and filename"""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    pytest_html = REPORT_DIR / "report.html"
    
    config.option.htmlpath = str(pytest_html)
    config.option.self_contained_html = True  # Critical for embedded images

def pytest_html_report_title(report):
    report.title = "Automation Test Report"

# ------- Ver 2.0 -----------------



# import pytest
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from datetime import datetime
# from pathlib import Path

# # Define base directory for reports & screenshots
# REPORT_DIR = Path("Reports", datetime.now().strftime("%Y%m%d_%H%M%S"))
# SCREENSHOT_DIR = REPORT_DIR / "screenshots"

# @pytest.fixture
# def driver():
#     """Fixture to initialize and quit WebDriver."""
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)  # Keep browser open (optional)

#     # Initialize the WebDriver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     yield driver  # Pass WebDriver instance to the test
#     driver.quit()


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Capture screenshots and debug embedding into HTML report."""
#     outcome = yield
#     report = outcome.get_result()
#     driver = item.funcargs.get("driver", None)

#     if report.when == "call" and driver:
#         # Create directories for reports and screenshots
#         SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
#         screenshot_path = SCREENSHOT_DIR / f"{item.name}.png"

#         # Save screenshot
#         driver.save_screenshot(str(screenshot_path))

#         # Debugging: Log the screenshot path
#         print(f"DEBUG: Screenshot saved at: {screenshot_path}")
#         if screenshot_path.exists():
#             print(f"DEBUG: Screenshot file exists at: {screenshot_path}")
#         else:
#             print(f"ERROR: Screenshot file was not saved!")

#         # Attach screenshot to HTML report
#         pytest_html = item.config.pluginmanager.getplugin("html")
#         if pytest_html:
#             extra = getattr(report, "extra", [])
            
#             # Create the absolute file path for embedding
#             absolute_path = screenshot_path.resolve().as_uri()
#             print(f"DEBUG: Absolute path for embedding: {absolute_path}")

#             # Embed into the HTML report
#             html = f'<div><img src="{absolute_path}" alt="screenshot" style="width:304px;height:228px;" ' \
#                    f'onclick="window.open(this.src)" align="right"/></div>'
#             extra.append(pytest_html.extras.html(html))
#             report.extra = extra



# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     """Set up the report directory and filename."""
#     REPORT_DIR.mkdir(parents=True, exist_ok=True)  # Ensure report directory exists
#     pytest_html = REPORT_DIR / "report.html"

#     config.option.htmlpath = str(pytest_html)  # Set HTML report path
#     config.option.self_contained_html = True


# def pytest_html_report_title(report):
#     """Customize the HTML report title."""
#     report.title = "Automation Test Report"



# ----------------- ---------------- -----------------
# ----------------- Screenshot/report working Not embedded -----------------
# # ----------------- ---------------- -----------------

# import pytest
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from datetime import datetime
# from pathlib import Path

# # Define base directory for reports & screenshots
# REPORT_DIR = Path("Reports", datetime.now().strftime("%d%m%Y_%H%M%S"))
# SCREENSHOT_DIR = Path(REPORT_DIR, "screenshots")

# @pytest.fixture
# def driver():
#     """Fixture to initialize and quit WebDriver."""
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)  # Keep browser open (optional)
    
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     yield driver  # Pass WebDriver instance to test
#     driver.quit()

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Capture and embed screenshots in the HTML report."""
#     outcome = yield
#     report = outcome.get_result()
#     driver = item.funcargs.get("driver", None)  # Get WebDriver from test function

#     if report.when == "call" and driver:
#         SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)  # Ensure screenshot directory exists

#         # Save screenshot
#         screenshot_path = SCREENSHOT_DIR / f"{item.name}.png"
#         driver.save_screenshot(str(screenshot_path))

#         # Embed screenshot in the HTML report
#         pytest_html = item.config.pluginmanager.getplugin("html")
#         if pytest_html:
#             extra = getattr(report, "extra", [])
#             relative_path = os.path.relpath(screenshot_path, os.getcwd()).replace("\\", "/")
#             html = f'<div><img src="{relative_path}" alt="screenshot" style="width:304px;height:228px;" ' \
#                    f'onclick="window.open(this.src)" align="right"/></div>'
#             extra.append(pytest_html.extras.html(html))
#             report.extra = extra

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     """Set up the report directory and filename."""
#     REPORT_DIR.mkdir(parents=True, exist_ok=True)  # Ensure report directory exists
#     pytest_html = REPORT_DIR / "report.html"

#     config.option.htmlpath = str(pytest_html)  # Set HTML report path
#     config.option.self_contained_html = True

# def pytest_html_report_title(report):
#     """Customize the HTML report title."""
#     report.title = "Automation Test Report"



# ----------------- ---------------- -----------------
# ----------------- Screenshot working -----------------
# # # ----------------- ---------------- -----------------
# import pytest
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture
# def driver():
#     """Fixture to initialize and quit WebDriver."""
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield driver  # Pass the driver to the test
#     driver.quit()  # Close the browser after the test

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Capture a screenshot and attach it to the HTML report."""
#     outcome = yield
#     report = outcome.get_result()
#     driver = item.funcargs.get("driver", None)  # Access the driver from the test function

#     # Take a screenshot if the driver is available
#     if report.when == "call" and driver:
#         screenshot_dir = "screenshots"
#         os.makedirs(screenshot_dir, exist_ok=True)

#         # Save the screenshot with the test name
#         screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
#         driver.save_screenshot(screenshot_path)

#         # Attach screenshot to the pytest-html report
#         pytest_html = item.config.pluginmanager.getplugin("html")
#         if pytest_html:
#             extra = getattr(report, "extra", [])
#             extra.append(pytest_html.extras.image(screenshot_path, mime_type="image/png"))
#             report.extra = extra