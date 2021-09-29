
import os

def get_base_url():
    env = os.environ.get('ENV','test')
    if env.lower() == 'test':
        return 'http://localhost:8888/demotestsite/'
    elif env.lower() == 'prod':
        return 'http://localhost:8888/prod/demotestsite/'
    else:
        raise Exception(f"Unknown environment: {env}")

def get_database_credentials():

    env = os.environ.get('ENV','test')
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    if not db_user or not db_password:
        raise Exception("Environment variables 'DB_USER' and 'DB_PASSWORD'"
                        "must be set")

    if env == 'test':
        db_host = '127.0.0.1'
        db_port = 8889
    elif env == 'prod':
        db_host = 'demostore.supersqa.com'
        db_port = 3306
    else:
        raise Exception(f"Unknown environment: {env}")

    db_info = {"db_host": db_host, "db_port": db_port,
               "db_user": db_user, "db_password": db_password}

    return db_info

#(venv_py3_sel) mneelaka@MNEELAKA-M-H1BQ ssqatest %export BROWSER='chrome'
#export DB_USER=root
#export DB_PASSWORD=root
#export RESULTS_DIR=/Users/mneelaka/PycharmProjects/python_selenium_course/ssqatest/results

#pytest -m tcid12 --alluredir=/Users/mneelaka/PycharmProjects/python_selenium_course/ssqatest/allure_reports
#allure serve /Users/mneelaka/PycharmProjects/python_selenium_course/ssqatest/allure_reports