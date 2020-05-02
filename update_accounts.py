from selenium import webdriver
import chromedriver_binary
import time
from common_module.login import *

def click_reloads(driver):
    elms = driver.find_elements_by_xpath("//input[@data-disable-with='更新']")
    for elm in elms:
        try:
            elm.click()
            time.sleep(1)
        except:
            continue
    time.sleep(5)

def main():
    target_url = "https://moneyforward.com/accounts"
    chrome_option = webdriver.ChromeOptions()
    # Chromeインスタンスを作成する

    driver = webdriver.Chrome(options=chrome_option)
    driver.get(target_url)
    driver = loginMoneyForward(driver)
    for i in range(3):
        click_reloads(driver)
        time.sleep(5)


main()