#VERIFICATORI
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import self as self


#implementam o clasa Login care sa mosteneasca uittest.TestCase
class Login(unittest.TestCase):

    LOGIN_BTN = (By.LINK_TEXT, 'Form Authentication')
    PAGE_TITLE = (By.LINK_TEXT, 'The Internet' )
    ERROR_MESSAGE = (By.XPATH,'/html/body/div[1]/div/div')
    SUCCESS_MESSAGE = (By.XPATH, '/html/body/div[1]/div/div')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.implicitly_wait(1)
        self.chrome.find_element(*self.LOGIN_BTN).click()

    def tearDown(self) -> None:
        self.chrome.quit()
    def test1(self):
        actual = self.chrome.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(actual, expected, 'Pagina nu exista')

    def test2(self):
        actual = self.chrome.title
        expected = "The Internet"
        self.assertEqual(actual, expected, 'Title is not ok')

    def test3(self):
        actual = self.chrome.find_element(By.XPATH, '//h2').text
        expected = 'Login Page'
        self.assertEqual(actual, expected, 'Error')
        print(actual)

    def test4(self):
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button').is_displayed()

    def test5(self):
        self.chrome.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').is_enabled()

    def test6(self):
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button').click()
        message = self.chrome.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(message.is_displayed(), 'Message is not there')

    def test7(self):
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[1]/div/input').send_keys('test@email')
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[2]/div/input').send_keys('parola')
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i').click()
        actual = self.chrome.find_element(By.XPATH, '/html/body/div[1]/div/div').text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    def test8(self):
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i').click()
        self.chrome.find_element(By.XPATH, '/html/body/div[1]/div/div/a').click()
        actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div/div'), 'Your username is invalid!'))
        if actual:
            print('Message is not there!')
        else:
            print('Message is there!')

    def test9(self):
        actual = [self.chrome.find_element(By.XPATH, '//label[@for="username"]').text,
                  self.chrome.find_element(By.XPATH, '//label[@for="password"]').text]
        expected = ['Username', 'Password']
        self.assertEqual(actual[0], expected[0], 'Username')
        self.assertEqual(actual[1], expected[1], 'Password')

    def test10(self):
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[1]/div/input').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[2]/div/input').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(actual, expected, 'The page is not correct.')
        WebDriverWait(self.chrome, 4).until(
            EC.presence_of_element_located((By.XPATH, '//div//div//div[@class="flash success"]')))
        logged_message = self.chrome.find_element(*self.SUCCESS_MESSAGE)
        self.assertTrue(logged_message.is_displayed(), 'You logged into a secure area!')
        check = self.chrome.find_element(By.XPATH, '/html/body/div[1]/div/div').text
        expected = 'secure area!'
        self.assertTrue(expected in check, 'Message ok.')

    def test11(self):
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[1]/div/input').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[2]/div/input').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i').click()
        self .chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/a/i').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'This page is not the right page!')

    def test12(self):
        # self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[1]/div/input').send_keys('tomsmith')
        text = self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/h4').text
        split_text = text.split()
        print(split_text)
        for split in split_text:
            self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[1]/div/input').send_keys('tomsmith')
            self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[2]/div/input').send_keys(split)
            self.chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button').click()
            if self.chrome.current_url == 'https://the-internet.herokuapp.com/secure':
                print(f'Parola secreta este {split}')
                break
            else:
                print('Nu am reusit sa gasesc parola.')


