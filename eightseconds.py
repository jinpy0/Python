def test1():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import json
    import openpyxl
    import csv

    url = "https://www.ssfshop.com/8seconds/MEN/list?dspCtgryNo=SFMA42&brandShopNo=BDMA07A01&brndShopId=8SBSS"
    html = urlopen(url)
    obj_list = BeautifulSoup(html, "html.parser")
    
    li_list = obj_list.select("#dspGood > li")
    
    # print(len(li_list))
    
    item_list = []
    
    for index, item in enumerate(li_list):
        name = item.select_one("a > div.info > span.name").text
        price = item.select_one("a > div.info > span.price").text
        dic = [name, price]
        item_list.append(dic)
        # print(f"{index}.{name}{price}")
    
    # csv 파일 저장
    header = ["제품명", "가격"]
    with open("wear.csv", "w", encoding="utf-8", newline="") as f:
        wt = csv.writer(f, quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
        wt.writerow(header)
        for item in item_list:
            wt.writerow(item)
    
    # json 파일 저장
    
    # 1. 딕셔너리로 만들기
    
    dic_list = []
    for item in item_list:
        dic = {}
        dic["제품명"]=item[0] 
        # 딕셔너리에 값을 주기 위해서는 key와 value를 대괄호로 줘야 함
        dic["가격"]=item[1]
        dic_list.append(dic)
        
    with open("wear.json", "w", encoding="utf-8") as f:
        json.dump(dic_list, f, ensure_ascii=False)
    
    # Excel 파일 저장    
    wb = openpyxl.Workbook()
    sheet = wb.create_sheet("제품 정보")
    
    sheet["A1"] = "제품명"
    sheet["B1"] = "가격"
    
    start_index = 2
    end_index = len(item_list) + start_index
    
    for i in range(start_index, end_index):
        ex_list = item_list[i-start_index]
        sheet[f"A{i}"] = ex_list[0]
        sheet[f"B{i}"] = ex_list[1]
        
    wb.save("wear.xlsx")
    
# test1()



