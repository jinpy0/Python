# 기말 범위 ~~ 

def test1():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    
    url = "https://www.naver.com/"
    html = urlopen(url)
    obj_list = BeautifulSoup(html, "html.parser")
    
    li_list = obj_list.select_one("#shortcutArea > ul")

# test1()

def test2():
    import pyautogui as pg
    import time
    
    # print(pg.size()) # 화면 해상도
    # print(pg.position()) # 마우스 위치
    
    # pg.moveTo(500,500) # 마우스 이동
    # pg.moveTo(500,500,2) # 3 번째 매개변수는 속도
    
    # pg.dragTo(500,500,2) # 마우스 드래그

    # pg.click() # 마우스 클릭
    # pg.click(button = "right") # 우측 버튼 클릭 # 기본값 : left
    # time.sleep(1)
    # pg.click()

    # pg.doubleClick() # 더블 클릭

    # pg.click(clicks = 3, interval= 1) # clicks : 클릭 횟수 , interval : 클릭 간격 (초)

# test2()

def test3():
    import pyautogui as pg
    import time
    import pyperclip
    
    # pg.write("Hello World!") # 출력

    # pg.write("Hello World!", interval=1)
    
    pyperclip.copy("안녕하세요!")

    pg.hotkey('ctrl', 'v')

# test3()

def test4():
    import pyautogui as pg
    
    # value = pg.alert(text = "내용입니다", title = "제목", button = "OK")
    # print(value)

    # value = pg.prompt(text = "내용입니다", title = "제목", default = "입력하세요")
    # print(value)

    # value = pg.confirm(text = "내용", title = "제목", buttons = ['OK', 'Cancel', 'NO'])
    # print(value)

    value = pg.password(text = "내용", title = "제목", default = "입력하세요", mask = "*")
    print(value)
    
# test4()

def test5():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    
    # 크롬 드라이버 자동 업데이트
    from webdriver_manager.chrome import ChromeDriverManager
    
    # 브라우저 생성 후 꺼짐
    # service = Service(executable_path=ChromeDriverManager().install())
    # browser = webdriver.Chrome(service=service)
    
    # 브라우저 생성 후 꺼짐 방지
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    
# test5()

def basic__setting():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)