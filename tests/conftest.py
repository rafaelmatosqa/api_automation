import pytest
import json
from utils.environment import get_config
from utils.api_client import APIClient
from utils.result_logger import ResultLogger
from utils.annotations import TestCase

@pytest.fixture(scope='session')
def config():
    return get_config()

@pytest.fixture(scope='session')
def jira_config():
    with open('tm4j_properties.json', 'r') as file:
        return json.load(file)

@pytest.fixture(scope='session')
def api_client(config):
    return APIClient(config.BASE_URL, config.API_KEY)

@pytest.fixture(scope='session')
def result_logger(jira_config):
    return ResultLogger(jira_config)

def pytest_runtest_logreport(report):
    if report.when == 'call':
        result_logger = report.config._result_logger
        status = 'passed' if report.outcome == 'passed' else 'failed'
        test_case_key = getattr(report.function, 'test_case_key', None)
        result_logger.log_result(report.nodeid, status, report.config._environment, test_case_key)

def pytest_sessionfinish(session, exitstatus):
    result_logger = session.config._result_logger
    result_logger.save_results()

def pytest_configure(config):
    config._result_logger = ResultLogger(jira_config())
    config._environment = get_config().__name__

