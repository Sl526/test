'''
url配置
'''

import pytest
from PageObjects.homePage import HomePage
from urllib.parse import urlparse, urlunparse

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="localhost",
        help="测试环境地址"
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="开启有头模式（显示浏览器窗口）"
    )

def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    
    parsed = urlparse(url)
    netloc = parsed.netloc
    
    if netloc and ":" not in netloc:
        netloc += ":8080"
    
    return urlunparse(parsed._replace(netloc=netloc))

@pytest.fixture
def homepage(request):
    raw_url = request.config.getoption("--url")
    full_url = normalize_url(raw_url)
    is_headed = request.config.getoption("--headed")
    hp = HomePage(url=full_url, headless=not is_headed)
    
    try:
        hp.click_login()
        hp.click_configure()
        yield hp
    finally:
        hp.quit_executor()