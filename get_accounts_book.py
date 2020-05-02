from selenium import webdriver
import chromedriver_binary
import pandas as pd
import re
from common_module.login import *


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
    dataframe = dataframe[~dataframe["金額（円）"].str.contains("(振替)")]
    dataframe["金額（円）"] = dataframe["金額（円）"].apply(int)
    return dataframe

#Todo 型変換がうまく行っていない
def get_spending(dataframe):
    dataframe = preprocessing_dataframe(dataframe)
    dataframe = dataframe[dataframe["金額（円）"] < 0]
    return dataframe

#Todo 型変換がうまく行っていない
def get_income(dataframe):
    dataframe = preprocessing_dataframe(dataframe)
    dataframe = dataframe[dataframe["金額（円）"] > 0]
    return dataframe

def main():
    target_url = "https://moneyforward.com/cf"

    driver = loginMoneyForward(target_url)
    dataframe = table2dataframe(driver)

    spending = get_spending(dataframe)
    income = get_income(dataframe)
    spending.to_csv("spending.csv")
    income.to_csv("income.csv")
main()