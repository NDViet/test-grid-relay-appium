# selenium.common.exceptions.SessionNotCreatedException: Message: Could not start a new session. Could not start a new session. Error while creating session with the service http://localhost:4723. Could not start a new session. Response code 500. Message: An unknown server-side error occurred while processing the command. Original error: The desired should not include both of an 'appPackage' and a 'browserName'
# Host info: host: '192.168.1.21', ip: '2402:800:62c0:97aa:85bb:50c5:2dd5:b7d9%en0'
# Build info: version: '4.30.0', revision: '509c7f1'
# System info: os.name: 'Mac OS X', os.arch: 'aarch64', os.version: '15.4', java.version: '17.0.11'
# Driver info: driver.version: unknown
# Build info: version: '4.30.0', revision: '509c7f1'
# System info: os.name: 'Mac OS X', os.arch: 'aarch64', os.version: '15.4', java.version: '17.0.11'
# Driver info: driver.version: unknown
# Build info: version: '4.30.0', revision: '509c7f1'
# System info: os.name: 'Mac OS X', os.arch: 'aarch64', os.version: '15.4', java.version: '17.0.11'
# Driver info: driver.version: unknown
# Stacktrace:
#     at org.openqa.selenium.grid.node.remote.RemoteNode.newSession (RemoteNode.java:167)
#     at org.openqa.selenium.grid.distributor.local.LocalDistributor.startSession (LocalDistributor.java:665)
#     at org.openqa.selenium.grid.distributor.local.LocalDistributor.newSession (LocalDistributor.java:584)
#     at org.openqa.selenium.grid.distributor.local.LocalDistributor$NewSessionRunnable.handleNewSessionRequest (LocalDistributor.java:848)
#     at org.openqa.selenium.grid.distributor.local.LocalDistributor$NewSessionRunnable.lambda$run$1 (LocalDistributor.java:805)
#     at java.util.concurrent.ThreadPoolExecutor.runWorker (ThreadPoolExecutor.java:1136)
#     at java.util.concurrent.ThreadPoolExecutor$Worker.run (ThreadPoolExecutor.java:635)
#     at java.lang.Thread.run (Thread.java:842)
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
