from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("Launching Chrome Browser...........")
    elif browser=="firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser...........")
    else:
        driver=webdriver.Chrome()
    return driver

#This will get the value from CLI /hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

#This will return the Browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

### pytest HTML Report

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'Entrata Assessment'
        config.stash[metadata_key]['Module Name'] = 'Demo Test'
        config.stash[metadata_key]['Tester'] = 'SD'

