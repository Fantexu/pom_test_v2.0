from selenium import webdriver


def get_driver(is_headless=False):
    # 后台运行
    if is_headless:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
    else:
        option = None
        
    return webdriver.Chrome(chrome_options=option)
