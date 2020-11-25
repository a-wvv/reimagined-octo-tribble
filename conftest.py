import pytest
from splinter import Browser

@pytest.fixture(scope='function')
def browser():
    browser = Browser('chrome')
    yield browser
    browser.quit()
