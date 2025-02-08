import platform
import sys
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

def before_all(context):
    print("BEFORE ALL")
    setup_browser(context)

def before_tag(context, tag):
    print("BEFORE TAG")

def before_feature(context, feature):
    print("BEFORE FEATURE")

def before_scenario(context, scenario):
    print("BEFORE SCENARIO")

def before_step(context, step):
    print("BEFORE STEP")

def after_step(context, step):
    print("AFTER STEP")

    if step.status == "failed" and hasattr(context, "driver") and context.driver:
        screenshot_name = f"scenario-{context.scenario.name}-step-{step.name}"
        allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)

def after_scenario(context, scenario):
    print("AFTER SCENARIO")

def after_feature(context, feature):
    print("AFTER FEATURE")

def after_tag(context, tag):
    print("AFTER TAG")

def after_all(context):
    print("AFTER ALL")
    teardown_browser(context)
    set_allure_environment_values(context)

# ----- Custom functions -----

def set_allure_environment_values(context):
    if hasattr(context, "driver") and context.driver:
        env_info = f"Browser = {context.browser.capitalize()}\nBrowser_Version = {context.driver.capabilities["browserVersion"]}\nOS_Platform = {platform.system()}\nPython_Version = {sys.version}"
    else:
        env_info = f"Browser = N/A\nBrowser_Version = N/A\nOS_Platform = {platform.system()}\nPython_Version = {sys.version}"

    try:
        filepath = "results/environment.properties"
        with open(filepath, 'w') as f:
            f.write(env_info)
        print(f"Environment file \"{filepath}\" created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the \"{filepath}\" file: {e}")

def setup_browser(context):
    # os.environ["browser"] = "chrome" # For testing, comment out before commiting.
    env_browser = os.environ.get("browser")

    if env_browser:
        context.browser = env_browser.casefold()

        if context.browser == "chrome":
            print(f"{context.browser.capitalize()} browser found, initializing.")
            setup_chrome(context)
        elif context.browser == "firefox":
            print(f"{context.browser.capitalize()} browser found, initializing.")
            setup_firefox(context)
    else:
        print("No browser found in environment variables.")

def setup_chrome(context):
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920,1200")
    context.driver = webdriver.Chrome(options=chrome_options)

def setup_firefox(context):
    firefox_options = FirefoxOptions()
    # firefox_options.add_argument("--headless")
    # driver.set_window_size(1920, 1080)
    context.driver = webdriver.Firefox(options=firefox_options)

def teardown_browser(context):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
