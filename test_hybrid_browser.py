from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.client_config import ClientConfig
import time

options = ChromeOptions()
options.set_capability("platformName", "Android")
options.set_capability("appium:platformVersion", "15")
options.set_capability("appium:automationName", "uiautomator2")

driver = None
capabilities = None
try:
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    capabilities = driver.capabilities
    driver.get('http://google.com')
    print(driver.title)
    time.sleep(10)
except Exception as e:
    raise e
finally:
    if capabilities is not None:
        print("Capabilities: ", capabilities)
    if driver is not None:
        driver.quit()