# -*- coding:utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# LAST_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

EXCUTABLE_PATH = "/root/app/cyanmori/chromedriver"
class chrome_driver():
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_argument("service_args = ['–ignore - ssl - errors = true', '–ssl - protocol = TLSv1']")
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('disable-infobars')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("detach", True)
        self.options.add_argument('--headless')
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        # path = '/home/workspace/flask_chrome'
        # prefs = {'profile.default_content_settings.popups': 0,
        #          'download.default_directory': '/home/workspace/flask_jump_url/download/'}
        # self.options.add_experimental_option('prefs', prefs)

    def selenium_out_url(self):
        driver = webdriver.Chrome(
            options=self.options,
            executable_path=EXCUTABLE_PATH,
            desired_capabilities=None)

        with open('/root/app/cyanmori/stealth.min.js') as f:
            js = f.read()

        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js
        })
        driver.set_page_load_timeout(60)
        return driver