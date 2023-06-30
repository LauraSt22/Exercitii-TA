#site-uri ce pot fi folosite
#https://www.phptravels.net/
# http://automationpractice.com/index.php
# https://formy-project.herokuapp.com/
# https://the-internet.herokuapp.com/
# https://www.techlistic.com/p/selenium-practice-form.html
# jules.app


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(ChromeDriverManager().install())

chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

#Locator by ID

# chrome.get("https://phptravels.net/login")
# chrome.find_element(By.ID, 'exampleInputEmail1').send_keys('example@email.com')
# sleep(3)
#
# chrome.get("https://phptravels.net/login")
# chrome.find_element(By.ID, "cookie_stop").click()
# sleep(5)

# chrome.get("https://formy-project.herokuapp.com/form")
# chrome.find_element(By.ID, 'first-name').send_keys('Laura')
# sleep(3)

#Locator by link text
# chrome.get("https://the-internet.herokuapp.com/")
# chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
# sleep(3)

# chrome.get("https://the-internet.herokuapp.com/")
# chrome.find_element(By.LINK_TEXT, 'Forgot Password').click()
# # sleep(3)
#
# chrome.get("https://formy-project.herokuapp.com/form")
# chrome.find_element(By.LINK_TEXT, 'Submit').click()
# sleep(3)

#Locator partial link text
# chrome.get("https://formy-project.herokuapp.com/")
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Autocompl').click()
# sleep(3)
#
# chrome.get("https://formy-project.herokuapp.com/")
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'own').click()
# sleep(3)

# chrome.get("https://jules.app/sign-in")
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()
# sleep(3)

#Locator by name
# chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
# chrome.find_element(By.NAME, 'firstname').send_keys('Maria')
# sleep(3)

# chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
# chrome.find_element(By.NAME, 'lastname').send_keys('Anton')
# sleep(3)

# chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
# chrome.find_element(By.NAME, 'continents').send_keys('Europe')
# sleep(3)

#Locator by tag
# chrome.get("https://formy-project.herokuapp.com/autocomplete")
# # chrome.find_elements(By.TAG_NAME, 'input')
# # chrome.find_element(By.TAG_NAME, 'input').send_keys('Test')
# input_list=chrome.find_elements(By.TAG_NAME, 'input')
# input_list[2].send_keys('Test')
# sleep(3)

# chrome.get("https://formy-project.herokuapp.com/keypress")
# # chrome.find_element(By.TAG_NAME, 'input').send_keys('full name')
# input_list=chrome.find_elements(By.TAG_NAME, 'input')
# input_list[0].send_keys('Full name 1')
# sleep(3)

# chrome.get("https://jules.app/sign-in")
# # chrome.find_elements(By.TAG_NAME, 'input')
# # chrome.find_element(By.TAG_NAME, 'input').send_keys('example@email.com')
# input_list=chrome.find_elements(By.TAG_NAME, 'input')
# input_list[0].send_keys('Test@email.com')
# input_list[1].send_keys('Test')
# sleep(3)

#Locator by class name
# chrome.get("https://formy-project.herokuapp.com/autocomplete")
# chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Test')
# sleep(3)

# chrome.get("https://jules.app/sign-in")
# chrome.find_element(By.CLASS_NAME, 'MuiInputBase-input').send_keys('ababadd@email.com')
# sleep(3)

# chrome.get("https://formy-project.herokuapp.com/form")
# chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('TestName')
# sleep(3)

#Locator by CSS
#by ID
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys('Last')
# sleep(3)

#by CLASS
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('AddressTest')
# sleep(3)

#atribut=valoare_partiala
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter address"]').send_keys('address1')
# chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*=" address"]').send_keys('street')
# sleep(3)


#Xpath-atribut-valoare
# chrome.get('https://formy-project.herokuapp.com/form')
# attibute = chrome.find_element(By.XPATH, '/html/body/div/form/div/div[1]/input').get_attribute("type")
# sleep(3)
# print(attibute)
#
# chrome.get('https://phptravels.net/')
# attibute = chrome.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div/div[1]/div/div/div/input').get_attribute("placeholder")
# sleep(3)
# print(attibute)

# chrome.get('https://the-internet.herokuapp.com/login')
# attibute = chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[1]/div/input').get_attribute("name")
# sleep(3)
# print(attibute)

# #Xpath-Get text of an element
# chrome.get('https://phptravels.net/')
# text = chrome.find_element(By.XPATH, '/html/body/section[4]/div/div/div[2]/div[1]/div/div[3]/div/a/p[1]').text
# sleep(3)
# print(text)
#
# chrome.get('https://formy-project.herokuapp.com/form')
# text = chrome.find_element(By.XPATH, '/html/body/div/nav/a').text
# sleep(3)
# print(text)

# chrome.get('https://the-internet.herokuapp.com/')
# text = chrome.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[1]/a').text
# sleep(3)
# print(text)

#Xpath-partial text
# chrome.get('https://jules.app/sign-in')
# text = chrome.find_element(By.XPATH, "//a[contains(text(), 'password')]").text
# sleep(3)
# print(text)

#Xpath-pipe/or operator
# chrome.get('https://jules.app/sign-in')
# chrome.find_element(By.XPATH, "//input[@aria-invalid='false']|//input[@autocomplete='on']|//input[@placeholder='Enter your email']").send_keys('email')
# sleep(3)

# #Xpath- * locator
# chrome.get('https://jules.app/sign-in')
# chrome.find_element(By.XPATH, "//*[contains(@placeholder, 'Enter')]").send_keys('test')
# sleep(3)

#Xpath- list elem
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# list = chrome.find_elements(By.XPATH, "(//input[@class='form-control'])[2]")
# sleep(1)
# print(list)

# #Xpath - parent locator
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, "(//input[@id='locality'])//parent::div")
# sleep(1)


#Xpath - sibling locator
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, "(//input[@id='locality'])/preceding-sibling::strong")
# sleep(1)
#
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, "(//input[@id='locality'])/preceding-sibling::strong/following-sibling::input").send_keys('City2')
# sleep(1)


# #Xpath - Axis navigation - 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
chrome.get('https://formy-project.herokuapp.com/autocomplete')
def formy_autocomplete(placeholder_input, value_input):
    my_input = chrome.find_element(By.XPATH, f"//input[@placeholder='{placeholder_input}']")
    my_input.clear()
    my_input.send_keys(value_input)


formy_autocomplete('Enter address', 'Test')
formy_autocomplete('Street address', 'Test2')
formy_autocomplete('Street address 2', 'Test3')
formy_autocomplete('City', 'Test4')
# sleep(3)
