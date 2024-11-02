from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import csv
import openpyxl

url = "https://anoblir.com/product/list.html?cate_no=205"
html = urlopen(url)
bs = BeautifulSoup(html.read(), "html.parser")

#contents > div.list-box > div.right-box > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul
li_list = bs.select("#contents > div.list-box > div.right-box > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li")
# print(len(li_list))
item_list = []
a = 1
for index, item in enumerate(li_list):
    #anchorBoxId_2051 > div.description > strong > a > span:nth-child(2)
    name = item.select_one("div.description > strong > a > span:nth-child(2)").text
    # print(f"{index}, {name}")
  
    #anchorBoxId_2051 > div.description > ul > li:nth-child(2) > span:nth-child(2)  
    price = item.select_one("div.description > ul > li:nth-child(2) > span:nth-child(2)").text
    # print(f"{name}, {price}")
    
    #anchorBoxId_2051 > div.description > ul > li:nth-child(3) > span
    try:
        sale_price = item.select_one("div.description > ul > li:nth-child(3) > span").text
    except:
        sale_price = price
    finally:
        # print(f"{index} : {sale_price}")
        dic = [name, price, sale_price]
        item_list.append(dic)

header = ["제품명", "정가", "할인가"]

with open("shirts.csv", "w", encoding = "utf-8", newline="")as f:
    writer = csv.writer(f, quotechar = '"', quoting = csv.QUOTE_NONNUMERIC)
    # quotechar = "'" 로 설정을 해놓으면 쉼표를 포함한 특수문자도 같이 quoting 됨
    writer.writerow(header)
    for item in item_list:
        writer.writerow(item)