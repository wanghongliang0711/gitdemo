from datetime import datetime
import os

#AOS系统版本
AOS_VERSION = "6"
#端口
Appium_Port = "4723"
#adb devices 命令获取
AOS_udid = "6TV44HNV5HAYVWZ9"
#442ad8ef
#vivo 6TV44HNV5HAYVWZ9
#测试软件包名
PackageName = "com.jkc.mitube"
#测试软件界面名
PageName = "com.mitac.mitube.SplashActivity"



# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#G:\PycharmPy36Workspaces\DRV_Link_Auto_Test
## 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
#报错截图目录
PICTURE_DIR = os.path.join(REPORT_DIR, 'picture')
# print(PICTURE_DIR)
#报错log目录
Log_DIR = os.path.join(REPORT_DIR, 'Log')
# print(Log_DIR)
# 当前时间
CURRENT_TIME = datetime.now().strftime('%y-%m-%d_%H-%M-%S')
# 报告名称
HTML_NAME = 'testReport{}.html'.format(CURRENT_TIME)

