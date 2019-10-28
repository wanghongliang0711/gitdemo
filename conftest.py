from appium import  webdriver
import pytest
import time,os
import subprocess
from common_method.common import launch_DrvLink
from configure.conf import PICTURE_DIR,Log_DIR
import logging
from py._xmlgen import html

logging.basicConfig(level = logging.INFO,format = '%(asctime)s -%(name)s  - %(levelname)s - %(message)s')
logger = logging.getLogger("conftest")

driver = None
logcat_file = None
poplog = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    global driver, logcat_file, poplog
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = os.path.join(PICTURE_DIR , (report.nodeid.replace("::", "_")+".png").split("/")[-1])
            print(file_name)
            # file_name = "1.png"
            logfilename = os.path.join(Log_DIR , (report.nodeid.replace("::", "_")+".log").split("/")[-1])
            print(logfilename)
            # logfilename = "F:/adblogcat" + "/" +"1.log"
            logcat_file = open(logfilename, 'w')
            logcmd = "adb logcat -v time"
            poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE,shell=True)

            _capture_screenshot(file_name)
            if file_name:
                # html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                #        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


def _capture_screenshot(name):
    # driver = launch_DrvLink()
    global driver
    if driver == None:
        raise Exception("没有launch_DrvLink ！！！！")
    else:
        return driver.get_screenshot_as_file(name)

@pytest.fixture(scope='function', autouse=True)
def app_driver():
    global driver , logcat_file , poplog
    print("*********launch_DRVLink***********")
    driver = launch_DrvLink()
    yield driver
    print('*********close DRVLink***********')
    driver.quit()
    if logcat_file != None:
        print("logcat_file.close()  # 关闭文件")
        logcat_file.close()  # 关闭文件
        logcat_file = None
    if poplog != None:
        print("poplog.terminate()  # 结束进程")
        poplog.terminate()  # 结束进程
        poplog = None

#似乎用不到了
# def close_driver():
#     global logcat_file , poplog
#     if logcat_file != None:
#         print("logcat_file.close()  # 关闭文件")
#         logcat_file.close()  # 关闭文件
#     if poplog != None:
#         print("poplog.terminate()  # 结束进程")
#         poplog.terminate()  # 结束进程

#修改Environment
def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "DRV Link"
    config._metadata['接口地址'] = '***********'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")
    # configure._metadata.pop("Plugins")
    # configure._metadata.pop("Python")
    # configure._metadata.pop("Platform")
    # configure._metadata.pop("Packages")


#修改Summary
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: SVD测试中心")])
    prefix.extend([html.p("测试人员: blake.wang")])

def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    # cells.insert(2, html.th('Test_nodeid'))
    cells.pop(-1)  # 删除link列
    # cells.pop(2)

def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    # cells.insert(2, html.td(report.nodeid))
    cells.pop(-1)  # 删除link列
    # cells.pop(2)








