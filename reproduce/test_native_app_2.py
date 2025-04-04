# Request stuck in queue without Node match due to `browserName` not set while Node stereotype set `browserName`
# Request caps
# {"appium:app":"https://github.com/saucelabs/my-demo-app-android/releases/download/2.2.0/mda-2.2.0-25.apk","appium:appPackage":"com.saucelabs.mydemoapp.android","appium:appWaitActivity":"*","appium:automationName":"uiautomator2","appium:platformVersion":"15","browserName":"","goog:chromeOptions":{"extensions":[],"args":[]},"pageLoadStrategy":"normal","platformName":"ANDROID"}
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

options = ChromeOptions()
options.set_capability("browserName", "")
options.set_capability("platformName", "Android")
options.set_capability("appium:platformVersion", "15")
options.set_capability("appium:automationName", "uiautomator2")
options.set_capability("appium:app", "https://github.com/saucelabs/my-demo-app-android/releases/download/2.2.0/mda-2.2.0-25.apk")
options.set_capability("appium:appPackage", "com.saucelabs.mydemoapp.android")
options.set_capability("appium:appWaitActivity", "*")

driver = None
capabilities = None
try:
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    capabilities = driver.capabilities
    time.sleep(10)
except Exception as e:
    raise e
finally:
    if capabilities is not None:
        print("Capabilities: ", capabilities)
    if driver is not None:
        driver.quit()
