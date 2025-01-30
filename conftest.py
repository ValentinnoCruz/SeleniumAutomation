
# --------- Working v2.0 ---------

import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_html import extras

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to attach multiple screenshots to the HTML report for each test.
    """
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        if hasattr(item, "screenshot_paths"):
            extra = getattr(result, "extra", [])
            for screenshot in item.screenshot_paths:
                extra.append(extras.png(screenshot))
            result.extra = extra



# ----------------- Pytest HTML Report Working  -----------------

# import pytest
# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from pytest_html import extras

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield driver
#     driver.quit()

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Hook to attach screenshots to the HTML report for pass or fail.
#     """
#     outcome = yield
#     result = outcome.get_result()

#     if result.when == "call":
#         # if you only want screenshots for failures, check result.failed
#         if result.failed or result.passed:
#             driver = item.funcargs.get("driver", None)
#             if driver is not None:
#                 screenshot_dir = "screenshots"
#                 os.makedirs(screenshot_dir, exist_ok=True)
#                 file_name = f"{item.name}_{int(time.time())}.png"
#                 file_path = os.path.join(screenshot_dir, file_name)
#                 driver.save_screenshot(file_path)

#                 # Attach to HTML report
#                 extra = getattr(result, "extra", [])
#                 extra.append(extras.png(file_path))
#                 result.extra = extra
