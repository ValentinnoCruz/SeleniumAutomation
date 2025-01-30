import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestUserLogin():
    def test_User_Login(self):

        # Initialize ChromeDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Open the login page
        driver.get("https://sprout-qa-2-wioqjc6rsa-wl.a.run.app/#/login")

        # Wait for the login page to load before interacting with the elements
        wait = WebDriverWait(driver, 10) # wait for 10 seconds
        email_input = wait.until(EC.presence_of_element_located((By.ID, "email"))) # wait for the email input field to load
        email_input.send_keys("QAStandard4@canon.com")
        
        # Wait for the password input field to load
        PW_input = wait.until(EC.presence_of_element_located((By.ID, "current-password")))
        PW_input.send_keys("Canon1234")

        # Click on the Login Button
        driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']").click()

        #Explicit wait for the 
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='user-role']"))
            )
            print("User logged in successfully")
        except Exception as e:
            assert False, "User login failed"

        # Wait and close browser
        time.sleep(2)
        driver.quit()
