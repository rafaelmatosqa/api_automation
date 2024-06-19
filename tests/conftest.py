import pytest
from utils.environment import get_config
from utils.api_client import APIClient
from utils.result_logger import ResultLogger

@pytest.fixture(scope='session')
def config():
    return get_config()

@pytest.fixture(scope='session')
def api_client(config):
    return APIClient(config.BASE_URL, config.API_KEY)

@pytest.fixture(scope='session')
def result_logger():
    return ResultLogger()

def pytest_runtest_logreport(report):
    if report.when == 'call':
        result_logger = report.config._result_logger
        status = 'passed' if report.outcome == 'passed' else 'failed'
        result_logger.log_result(report.nodeid, status, report.config._environment)

def pytest_sessionfinish(session, exitstatus):
    result_logger = session.config._result_logger
    result_logger.save_results()

def pytest_configure(config):
    config._result_logger = ResultLogger()
    config._environment = get_config().__name__
