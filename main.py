from selenium import webdriver
import chromedriver_binary
from login_information.login import *

def loginMoneyForward(target_url):
    chrome_option = webdriver.ChromeOptions()
    # Chromeインスタンスを作成する
    driver = webdriver.Chrome(options = chrome_option)
    driver.get(target_url)

    #e-mailアドレスでログインを選択
    login_button = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/section/div/div/div[2]/div/a[1]")
    login_button.click()

    #emailアドレスの入力
    email = driver.find_element_by_name("mfid_user[email]")
    email.send_keys(EMAIL_ADDRESS)
    login_email_button = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input")
    login_email_button.click()

    #passwordの入力
    password = driver.find_element_by_name("mfid_user[password]")
    password.send_keys(PASSWORD)
    login_password_button = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input")
    login_password_button.click()



target_url = "https://moneyforward.com/cf"
loginMoneyForward(target_url)