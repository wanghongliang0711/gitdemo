import pytest,logging,time
from common_method.common import DriverWait_click_ById,elements_num_ById,swipeRight
from appium.webdriver.common.touch_action import TouchAction

logging.basicConfig(level = logging.INFO,format = '%(asctime)s -%(name)s  - %(levelname)s - %(message)s')
logger = logging.getLogger("test_TestID_W7")


def test_show_or_hide(app_driver):
    """side menu can show or hide"""
    DriverWait_click_ById(app_driver,"com.jkc.mitube:id/buttonLeftOnlyImage")
    logger.info("********tap the Menu icon********")
    elements_num_ById(app_driver, 'com.jkc.mitube:id/row_title',3)
    logger.info("********side menu can show********")
    DriverWait_click_ById(app_driver,"com.jkc.mitube:id/buttonLeftOnlyImage")
    logger.info("********tap the Menu icon********")
    elements_num_ById(app_driver, 'com.jkc.mitube:id/row_title',0)
    logger.info("********side menu can hide********")
    swipeRight(app_driver)
    logger.info("********swipe Right********")
    elements_num_ById(app_driver, 'com.jkc.mitube:id/row_title', 3)
    logger.info("********side menu can show********")
    TouchAction(app_driver).tap(x=(app_driver.get_window_size()['width'] - 10),
                            y=(app_driver.get_window_size()['height'] / 2)).perform()
    logger.info("********tap the area outside the Side menu********")
    elements_num_ById(app_driver, 'com.jkc.mitube:id/row_title', 0)
    logger.info("********side menu can hide********")
    logger.info("********test_show_or_hide PASS********")
    # raise Exception("launch_DrvLink 失败")




if __name__ == '__main__':
    pytest.main(['-v', 'test_TestID_W7.py'])







