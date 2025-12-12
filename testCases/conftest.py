import pytest
from selenium import webdriver
from datetime import datetime
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching firefox browser")
    else:
        driver=webdriver.Ie()
        print("default Launching IE browser")
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
######PYTEST HTML REPORT ########
# #it is hook for adding env report into HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name']='nop commerce'
#     config._metadata['Module']='Customers'
#     config._metadata['Tester']='Mahi'
# # it is hook for deleting or modifying env info to html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)


def pytest_html_report_title(report):
    report.title = "nopCommerce Automation Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project Name: nop commerce"])
    prefix.extend([f"Module : Customers"])
    prefix.extend([f"Environment : QA"])
    prefix.extend([f"Tester : Maheswari"])
    prefix.extend([f"Generated On : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"])
