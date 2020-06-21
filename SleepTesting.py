import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://itorrents.org/torrent/40A027E19E4A8022B6C6354A5F303F31E40E9582.torrent")
time.sleep(10)
