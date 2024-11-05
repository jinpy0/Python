def basic__setting():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    # 웹 브라우저를 그대로 받아옴 ( 동적 페이지로 )


def test1():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    browser.get("https://www.naver.com/") # 웹 페이지로 이동
        
#     #shortcutArea > ul
#     #shortcutArea > ul > li:nth-child(1)
    menu_list = browser.find_elements(By.CSS_SELECTOR, "#shortcutArea > ul > li")
    # 리턴되는 
    
    for menu in menu_list:
        try:
            serviceName = menu.find_element(By.CSS_SELECTOR, "a > span.service_name").text
        #shortcutArea > ul > li:nth-child(1) > a > span.service_name
        except:
            serviceName = ""
        print(serviceName)
        
test1()

