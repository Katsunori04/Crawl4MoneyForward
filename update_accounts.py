
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

    driver = loginMoneyForward(target_url)
    for i in range(3):
        click_reloads(driver)
        time.sleep(2)


main()