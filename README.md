# Introduction

Local setup to get started a simple Appium tests (hybrid browser or native app) through Selenium Grid (use Relay Node).

# Prerequisites

1. Download latest server jar to start the Selenium Grid.

```shell
wget https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.30.0/selenium-server-4.30.0.jar
```

Or copy a jar from local snapshot built.

2. Install Appium server and driver (uiautomator2 in this example)

```shell
npm install -g appium
```

```shell
appium driver install uiautomator2
```

3. Start Appium server (with chromedriver autodownload - for hybrid browser session)

```shell
appium server --allow-insecure chromedriver_autodownload
```

4. Start Grid Hub

```shell
java -jar selenium-server-4.30.0.jar hub
```

5. Start Relay Node

```shell
java -jar selenium-server-4.30.0.jar node --config config_relay.toml
```

In this example, we use `config_relay.toml` to configure the Relay Node with
- 1 slot capabilities can take both request for hybrid browser and native app (API version 15)
- 1 slot capabilities can take request for native app only (API version 14)

6. Use Android Studio to start 2 emulators with API version 15 and 14.

7. Grid is ready with Relay Node which has 2 slots.

```json
{
  "value": {
    "ready": true,
    "message": "Selenium Grid ready.",
    "nodes": [
      {
        "id": "d3d85a08-4154-422c-9027-0d860fa6b357",
        "uri": "http://192.168.1.9:5555",
        "maxSessions": 2,
        "sessionTimeout": 300000,
        "osInfo": {
          "arch": "aarch64",
          "name": "Mac OS X",
          "version": "15.4"
        },
        "heartbeatPeriod": 60000,
        "availability": "UP",
        "version": "4.31.0-SNAPSHOT (revision Unknown)",
        "slots": [
          {
            "id": {
              "hostId": "d3d85a08-4154-422c-9027-0d860fa6b357",
              "id": "f6366e7c-ce2c-4d32-b9f8-84cebef93f1b"
            },
            "lastStarted": "1970-01-01T00:00:00Z",
            "session": null,
            "stereotype": {
              "appium:automationName": "uiautomator2",
              "appium:platformVersion": "14",
              "myApp:publish": "public",
              "myApp:version": "beta",
              "platformName": "ANDROID"
            }
          },
          {
            "id": {
              "hostId": "d3d85a08-4154-422c-9027-0d860fa6b357",
              "id": "a68d986d-a1dd-42d4-b7c0-30b46fed7645"
            },
            "lastStarted": "1970-01-01T00:00:00Z",
            "session": null,
            "stereotype": {
              "appium:automationName": "uiautomator2",
              "appium:platformVersion": "15",
              "browserName": "chrome",
              "myApp:publish": "public",
              "myApp:version": "beta",
              "platformName": "ANDROID"
            }
          }
        ]
      }
    ]
  }
}
```

8. Run the test native app test

```shell
python test_native_app.py
```

It can be run in both 2 slots of the Relay Node (by random API version in client code).

9. Run the test hybrid browser test

```shell
python test_hybrid_browser.py
```

It can be run in the slot of the Relay Node which has API version 15 (since `browserName` is not set in Node stereotype).