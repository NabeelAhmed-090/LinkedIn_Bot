from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def connect_button(all_buttons_list):
    connect_buttons = []
    for btns in all_buttons_list:
        if btns.text == "Connect":
            connect_buttons.append(btns)
    return connect_buttons


def profile_button(all_buttons_list):
    for btns in all_buttons_list:
        if btns.text == "Me":
            return btns


def signOutbtn(all_buttons_list):
    for btns in all_buttons_list:
        if btns.text == "Sign Out":
            return btns


ser = Service("C:\\Users\\Dell\\OneDrive\\Desktop\\ChromeDriver\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

email = driver.find_element(By.NAME, "session_key")
password = driver.find_element(By.NAME, "session_password")

userEmail = input("Enter Email : ")
userPassword = input("Enter password : ")

email.send_keys(userEmail)
password.send_keys(userPassword)

signInButton = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
signInButton.click()

time.sleep(5)
currentUrl = driver.current_url

if "checkpoint/challenge/" in currentUrl:
    confirmationCode = driver.find_element(By.XPATH, '//*[@id="input__phone_verification_pin"]')
    verificationKey = input("Enter the verification code : ")
    confirmationCode.send_keys(verificationKey)
    submitButton = driver.find_element(By.XPATH, "//*[@id='two-step-submit-button']")
    submitButton.click()

driver.find_element(By.XPATH, "//*[@id='ember19']").click()
time.sleep(5)

all_buttons = driver.find_elements(By.TAG_NAME, "button")
connectButton = connect_button(all_buttons)

iterations = 0
for btn in connectButton:
    driver.execute_script("arguments[0].click();", btn)
    iterations += 1
    if iterations > 25:
        break
    time.sleep(2)


driver.close()



