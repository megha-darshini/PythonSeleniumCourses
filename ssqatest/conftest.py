
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Choptions
from selenium.webdriver.firefox.options import Options as FFoptions

import os,allure

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome','ch','headlesschrome','firefox','ff','headlessfirefox']

    browser = os.environ.get('BROWSER',None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set")\

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser} is not supported."
                        f"The supported browsers are: {supported_browsers}")

    if browser in ('chrome','ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox','ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = Choptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('headlessfirefox'):
        ffoptions = FFoptions()
        ffoptions.add_argument('--disable-gpu')
        ffoptions.add_argument('--no-sandbox')
        ffoptions.add_argument('--headless')
        driver = webdriver.firefox(options=ffoptions)

    request.cls.driver = driver
    yield
    driver.quit()

'''
#For pytest-html report only
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        #check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    raise Exception("Environment variables 'RESULTS_DIR' must be set")
                screenshot_path = os.path.join(results_dir,item.name + '.png')
                driver_fixture = item.funcargs['request']
                driver = driver_fixture.cls.driver.save_screenshot(screenshot_path)
            # only add additional html on failure
            #extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            #extra.append(pytest_html.extras.image("/Users/mneelaka/PycharmProjects/python_selenium_course/ssqatest/image.jpeg"))
            extra.append(pytest_html.extras.image("screenshot_path"))

        report.extra = extra
'''

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        # always add url to report
        xfail = hasattr(report, "wasxfail")
        #check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    raise Exception("Environment variables 'RESULTS_DIR' must be set")
                screenshot_path = os.path.join(results_dir,item.name + '.png')
                driver_fixture = item.funcargs['request']
                driver = driver_fixture.cls.driver.save_screenshot(screenshot_path)
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name='screenshot',attachment_type=allure.attachment_type.PNG)
#(venv_py3_sel) mneelaka@MNEELAKA-M-H1BQ ssqatest %export BROWSER='chrome'
#export DB_USER=root
#export DB_PASSWORD=root
#export RESULTS_DIR=/Users/mneelaka/PycharmProjects/python_selenium_course/ssqatest/results
#pytest -m tcid12 -W ignore::pytest.PytestUnknownMarkWarning

#pytest -m tcid12 -s --pdb --html=results/my_report.html --self-contained-html
#pytest -m tcid13 -s --pdb --html=results/my_report.html --self-contained-html
#pytest -m tcid33 -s --pdb --html=results/my_report.html --self-contained-html


#pytest -m tcid12 --alluredir=/Users/mneelaka/PycharmProjects/python_selenium_course/ssqatest/allure_reports
#allure serve

#https://pypi.org/project/pytest-html/
#https://pytest-html.readthedocs.io/en/latest/user_guide.html
#https://docs.qameta.io/allure/