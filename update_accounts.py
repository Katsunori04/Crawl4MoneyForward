
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

    #連続で更新するとエラーが発生する場合があるため、更新処理を5回試行
    for i in range(5):
        click_reloads(driver)


main()