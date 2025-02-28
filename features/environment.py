import platform
import sys
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import os

def before_all(context):
    context.browser = os.environ.get("BROWSER", "chrome").casefold().capitalize()

def before_scenario(context, scenario):
    if "no-ui" not in scenario.tags:
        setup_browser(context)

def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver") and context.driver:
        screenshot_name = f"scenario-{context.scenario.name}-step-{step.name}"
        allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)

def after_scenario(context, scenario):
    if "no-ui" not in scenario.tags:
        teardown_browser(context)

def after_all(context):
    set_allure_environment_values(context)

# ----- Custom functions -----

def set_allure_environment_values(context):
    env_info = f"Browser = {context.browser.capitalize()}\nOS_Platform = {platform.system()}\nPython_Version = {sys.version}"

    try:
        filepath = "results/environment.properties"
        with open(filepath, 'w') as f:
            f.write(env_info)
        print(f"Environment file \"{filepath}\" created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the \"{filepath}\" file: {e}")

def setup_browser(context):
    if context.browser == "Chrome":
        print(f"{context.browser} browser found, initializing.")
        setup_chrome(context)
    elif context.browser == "Firefox":
        print(f"{context.browser} browser found, initializing.")
        setup_firefox(context)
    else:
        print("No browser found in environment variable.")

def setup_chrome(context):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920,1200")
    chrome_service = ChromeService(executable_path="/usr/local/bin/chromedriver")
    context.driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

def setup_firefox(context):
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    # firefox_options.add_argument("--window-size=1920,1200")
    firefox_service = FirefoxService(executable_path="/usr/local/bin/geckodriver")
    context.driver = webdriver.Firefox(options=firefox_options, service=firefox_service)

def teardown_browser(context):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
