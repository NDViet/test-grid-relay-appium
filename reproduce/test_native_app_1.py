# This only open Chrome browser in emulator but didn't open the app
# Capabilities:  {'app': 'https://github.com/saucelabs/my-demo-app-android/releases/download/2.2.0/mda-2.2.0-25.apk', 'appWaitActivity': '*', 'appium:app': 'https://github.com/saucelabs/my-demo-app-android/releases/download/2.2.0/mda-2.2.0-25.apk', 'appium:appWaitActivity': '*', 'appium:automationName': 'uiautomator2', 'appium:platformVersion': '15', 'automationName': 'uiautomator2', 'browserName': 'chrome', 'databaseEnabled': False, 'desired': {'browserName': 'chrome', 'goog:chromeOptions': {'extensions': [], 'args': []}, 'pageLoadStrategy': 'normal', 'platformName': 'ANDROID', 'app': 'https://github.com/saucelabs/my-demo-app-android/releases/download/2.2.0/mda-2.2.0-25.apk', 'appWaitActivity': '*', 'automationName': 'uiautomator2', 'platformVersion': '15', 'appPackage': 'com.android.chrome', 'appActivity': 'com.android.chrome/com.google.android.apps.chrome.Main'}, 'deviceApiLevel': 35, 'deviceManufacturer': 'Google', 'deviceModel': 'sdk_gphone64_arm64', 'deviceName': 'emulator-5556', 'deviceScreenDensity': 480, 'deviceScreenSize': '1344x2992', 'deviceUDID': 'emulator-5556', 'goog:chromeOptions': {'extensions': [], 'args': []}, 'javascriptEnabled': True, 'locationContextEnabled': False, 'networkConnectionEnabled': True, 'pageLoadStrategy': 'normal', 'pixelRatio': '3', 'platform': 'LINUX', 'platformName': 'ANDROID', 'platformVersion': '15', 'se:bidiEnabled': False, 'se:cdp': 'ws://192.168.1.21:4444/session/09862bd8-8716-4e36-8410-b61ddc88d3e5/se/cdp', 'statBarHeight': 151, 'takesScreenshot': True, 'viewportRect': {'left': 0, 'top': 151, 'width': 1344, 'height': 2841}, 'warnings': {}, 'webStorageEnabled': False}
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

options = ChromeOptions()
options.set_capability("platformName", "Android")
options.set_capability("appium:platformVersion", "15")
options.set_capability("appium:automationName", "uiautomator2")
options.set_capability("appium:app", "https://github.com/saucelabs/my-demo-app-android/releases/download/2.2.0/mda-2.2.0-25.apk")
# options.set_capability("appium:appPackage", "com.saucelabs.mydemoapp.android")
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
