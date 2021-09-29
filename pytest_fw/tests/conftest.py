from config import Config
from pytest import fixture
from selenium import webdriver
import json

data_path = '/Users/mneelaka/PycharmProjects/python_selenium_course/pytest_fw/tests/test_data.json'

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     help="Environment to run tests against"
                     )

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg

def load_test_data(path):
    with open(path) as data_file:
        data  = json.load(data_file)
        return data

@fixture(params=[webdriver.Chrome])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data