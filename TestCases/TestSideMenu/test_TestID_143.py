import pytest,logging,time
from common_method.common import DriverWait_click_ById,DriverWait_click_ById_orders,Check_Str_ById


logging.basicConfig(level = logging.INFO,format = '%(asctime)s -%(name)s  - %(levelname)s - %(message)s')
logger = logging.getLogger("test_TestID_143")

def  test_copyright(app_driver):
    """copyright can be shown in about screen correctly"""
    DriverWait_click_ById(app_driver,"com.jkc.mitube:id/buttonLeftOnlyImage")
    DriverWait_click_ById_orders(app_driver,"com.jkc.mitube:id/row_title",1)
    DriverWait_click_ById(app_driver,"com.jkc.mitube:id/btnAbout")
    Check_Str_ById(app_driver,"com.jkc.mitube:id/textView","© 2017 JVCKENWOOD Corporation. All Rights Reserved.")
    logger.info("test_TestID_143 PASS")


if __name__ == '__main__':
    pytest.main(['-v', 'test_TestID_143.py'])