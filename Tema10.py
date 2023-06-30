import unittest
import HtmlTestRunner
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
import os
from pathlib import Path

# Ex 1

from Teme.Tema9 import Login
from Intalnirea10.test_alerts import Alerts
from Intalnirea10.test_keys import Keyboard
from Intalnirea10.test_context_menu import ContextMenu
from Intalnirea10.test_auth import Authentication
#from Intalnirea10.test_browser import Browser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Screenshot import Screenshot
from selenium.webdriver.common.keys import Keys


class TestSuite(unittest.TestCase):
    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
        #    unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
        #     unittest.defaultTestLoader.loadTestsFromTestCase(Authentication)
      #      unittest.defaultTestLoader.loadTestsFromTestCase(Browser),
        ])

        runner = HtmlTestRunner.HTMLTestRunner\
                (
            combine_reports=True,
            report_title='TestReport',
            report_name='Testing OK'
        )

        runner.run(teste_de_rulat)



# Ex 2

# https://formy-project.herokuapp.com/

class testing(unittest.TestCase):
    PAGE = (By.LINK_TEXT, 'Digest Authentication')
    USERNAME = 'admin'
    PASSWORD = 'admin'
    ADD_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/button')
    DEL_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/div/button')

    def setUp(self) -> None:
        s = Service(GeckoDriverManager().install())
        self.firefox = webdriver.Firefox(service=s)
        self.firefox.maximize_window()
        self.firefox.get('https://the-internet.herokuapp.com/')
        self.firefox.implicitly_wait(1)

    def tearDown(self) -> None:
        self.firefox.quit()

    def log_in(self):
        self.firefox.get("https://"  + self.USERNAME + ':' + self.PASSWORD + "@the-internet.herokuapp.com/digest_auth")
        sleep(3)
        actual = WebDriverWait(self.firefox, 2).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[2]/div/div/p'),
                                                                                       "Congratulations! You must "
                                                                                       "have the proper credentials."))

        if actual:
            print('The displayed message is correct.')
        else:
            print('The displayed message is not correct.')

    def elements(self):
        self.firefox.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        sleep(1)
        self.firefox.find_element(*self.ADD_BUTTON).click()
        sleep(1)
        self.firefox.find_element(*self.DEL_BUTTON).click()
        sleep(1)
        self.firefox.find_element(*self.ADD_BUTTON).click()
        sleep(1)
        self.firefox.find_element(*self.DEL_BUTTON).click()
        sleep(1)

    def file_download(self):
        self.firefox.find_element(By.LINK_TEXT, 'File Download').click()
        self.firefox.find_element(By.LINK_TEXT, 'sample.png').click()
        if os.path.exists(r"C:\Users\laura\Downloads\sample.png"):
            print('The file was downloaded.')
        else:
            print('The file was not downloaded.')
        self.firefox.find_element(By.LINK_TEXT, 'flower.jpeg').click()
        if os.path.exists(r"C:\Users\laura\Downloads\flower.jpeg"):
            print('The file was downloaded.')
        else:
            print('The file was not downloaded.')