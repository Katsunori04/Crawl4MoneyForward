import time

from login_information.login import *

def loginMoneyForward(driver):

    #e-mailアドレスでログインを選択
    login_button = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/section/div/div/div[2]/div/a[1]")
    login_button.click()
    time.sleep(1)

    #emailアドレスの入力
    email = driver.find_element_by_name("mfid_user[email]")
    email.send_keys(EMAIL_ADDRESS)
    login_email_button = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input")
    login_email_button.click()
    time.sleep(1)
    #passwordの入力
    password = driver.find_element_by_name("mfid_user[password]")
    password.send_keys(PASSWORD)
    login_password_button = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input")
    login_password_button.click()
    time.sleep(1)
    return driver