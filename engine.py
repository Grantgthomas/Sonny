from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

def engineInit(site):
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Firefox(service=service,options=options)
    driver.get(site[0])
    return driver
