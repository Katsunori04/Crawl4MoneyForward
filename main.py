from selenium import webdriver
import chromedriver_binary
import pandas as pd
import re
#パスワードを配置
from login_information.login import *

def loginMoneyForward(driver):

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

    return driver


def table2dataframe(driver):
    #Tableを解析
    table = driver.find_element_by_id("cf-detail-table")

    #Tableのヘッダーをリスト化
    thead = table.find_element_by_tag_name("thead").find_element_by_tag_name("tr").find_elements_by_tag_name("th")
    header_list = []
    for elm in thead:
       header_list.append(elm.text)

    #TableのBodyをリスト化
    tbody = table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
    elms_list = []
    for rows in tbody:
        row = rows.find_elements_by_tag_name("td")
        elms = []
        for elm in row:
            elms.append(elm.text)
        elms_list.append(elms)

    dataframe = pd.DataFrame(elms_list, columns=header_list)
    return dataframe

def preprocessing_dataframe(dataframe):
    #Columnの\n以降の文字列を削除
    dataframe = dataframe.rename(columns=lambda column: re.sub("\n.*", "", column))
    dataframe = dataframe[["日付", "内容", "金額（円）","保有金融機関", "大項目", "中項目"]]
    return dataframe


def main():
    target_url = "https://moneyforward.com/cf"
    chrome_option = webdriver.ChromeOptions()
    # Chromeインスタンスを作成する
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(target_url)
    driver = loginMoneyForward(driver)
    dataframe = table2dataframe(driver)

    dataframe= preprocessing_dataframe(dataframe)
    print(dataframe)
main()