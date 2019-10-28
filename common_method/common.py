import time
from appium import  webdriver
import logging
from selenium.webdriver.support.wait import WebDriverWait
from configure.conf import AOS_VERSION,PackageName,PageName,Appium_Port,AOS_udid
logging.basicConfig(level = logging.INFO,format = '%(asctime)s -%(name)s  - %(levelname)s - %(message)s')
logger = logging.getLogger("common")

#连接appium服务器
def launch_DrvLink():
    try:
        # 配置基本信息
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = AOS_VERSION
        desired_caps['deviceName'] = AOS_udid
        desired_caps['udid'] = AOS_udid
        # 包名/界面名
        desired_caps['appPackage'] = PackageName
        desired_caps['appActivity'] = PageName
        desired_caps['noReset'] = True  # 不清空缓存数据
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        driver = webdriver.Remote('http://localhost:'+Appium_Port+'/wd/hub' , desired_caps)
        time.sleep(2)
        return  driver
    except Exception as e:
        # logger.warning("launch_DrvLink Something maybe fail." + str(e))
        raise Exception("launch_DrvLink 失败 ", e)
        # return  None


#显示等待并点击按钮by id
def DriverWait_click_ById(app_driver,str_id):
    try:
        search_button = WebDriverWait(app_driver, 10).until(
            lambda x: x.find_element_by_id(str_id))
        time.sleep(1)  # 不等待有时候点了没反应
        search_button.click()
    except Exception as e:
        # logger.warning("DriverWait_click_ById." , e)
        raise Exception("DriverWait_click_ById 失败" , e)

#显示等待并点击按钮by xpath
def DriverWait_click_ByXpath(app_driver,str_xpath):
    try:
        search_button = WebDriverWait(app_driver, 10).until(
            lambda x: x.find_element_by_xpath(str_xpath))
        time.sleep(1)  # 不等待有时候点了没反应
        print(str_xpath)
        print(search_button.text)
        search_button.click()
    except Exception as e:
        # logger.warning("DriverWait_click_ById." , e)
        raise Exception("DriverWait_click_ByXpath 失败" , e)

def elements_num_ById(app_driver ,str_id , num):
    try:
        if num!=0:
            search_button = WebDriverWait(app_driver, 10).until(
                lambda x: x.find_elements_by_id(str_id))
        else:
            time.sleep(1)
            search_button = app_driver.find_elements_by_id(str_id)
        if len(search_button) == num:
            pass
        else:
            assert num == len(search_button), "side menu can not show, num is "+str(num)+", len is "+str(len(search_button))
    except Exception as e:
        # logger.warning("elements_num_ById." ,e)
        raise Exception("elements_num_ById 失败",e)

'''向左滑动方法'''
def swipeLeft(app_driver,t=600,n=1):
    try:
        l = app_driver.get_window_size()
        print(l)  # dict{'width': 720, 'height': 1280}
        x1 = l['width'] *  0.75  # 获取宽度x1
        y1 = l['height'] * 0.5  # 起始值y1
        x2 = l['width'] * 0.25  # 结束值y2
        for i in range(n):
            app_driver.swipe(x1, y1, x2, y1,duration=t)
    except Exception as e:
        # logger.warning("swipeLeft." ,e)
        raise Exception("swipeLeft 失败" ,e)

'''向右滑动方法'''
def swipeRight(app_driver,t=600,n=1):
    try:
        l = app_driver.get_window_size()
        # print(l)  # {'width': 1532, 'height': 2560}
        x1 = l['width']  * 0.25  # 获取宽度x1
        y1 = l['height'] * 0.5  # 起始值y1
        x2 = l['width'] * 0.75  # 结束值y2
        # print(x1,y1,x2 )
        for i in range(n):
            app_driver.swipe(x1, y1, x2, y1,duration=t)
    except Exception as e:
        # logger.warning("swipeRight." ,e)
        raise Exception("swipeRight 失败" ,e)

'''检查字符串 ById'''
def Check_Str_ById(app_driver,id,spec_str):
    try:
        search = WebDriverWait(app_driver, 10).until(
            lambda x: x.find_element_by_id(id))
        if  search.text.strip().replace('\n', '').replace('\r', '') != spec_str:
            raise Exception("字符串不匹配，text is "+str(search.text)+", spec_str is " + spec_str)
            # assert search.text == str,"字符串不匹配，text is "+str(search.text)+", str is " + str
    except Exception as e:
        # logger.warning("DriverWait_click_ById." , e)
        raise Exception("Check_Str_ById 失败", e)

def DriverWait_click_ById_orders(app_driver,id,num):
    try:
        search_button = WebDriverWait(app_driver, 10).until(
            lambda x: x.find_elements_by_id(id))
        time.sleep(1)  # 不等待有时候点了没反应
        search_button[num].click()
    except Exception as e:
        # logger.warning("DriverWait_click_ById." , e)
        raise Exception("DriverWait_click_ById 失败" , e)














