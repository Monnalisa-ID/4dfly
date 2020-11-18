import time,sys,random,os
import requests
from fake_useragent import UserAgent
from multiprocessing.pool import ThreadPool
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
ua = UserAgent()
a = ua.random
user_agent = ua.random
print (user_agent)
class bot:
    def __init__(self):
        self.add_argument(f'user-agent={user_agent}')
        self.add_argument('--ignore-certificate-errors')
        self.add_argument('--allow-running-insecure-content')
        self.add_argument("--proxy-server='direct://'")
        self.add_argument("--proxy-bypass-list=*")
        self.add_argument("--start-maximized")
        self.add_argument('--disable-gpu')
        self.add_argument('--disable-dev-shm-usage')
        self.add_argument('--no-sandbox')

        #self.driver.get('http://raboninco.com/1sLv9')
bot()

opts = Options()

opts.add_extension('./buster_ext.crx')
opts.add_argument('--ignore-ssl-erros')
print ('OTW TUYUL BOSQUE....')
driver = webdriver.Chrome(chrome_options=opts)
driver.get('http://raboninco.com/1sLv9')
path = "/html/body/div[6]/table/tbody/tr[1]/td/div/div[1]/span[2]/a/img"
delay = 10 #Delay
try:
    element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, path)))
    element.click()
    print ('OTW MENUYUL BOSQUE....')
finally:
    print('MISI SELESAI BOSQUE...')
    time.sleep(3)
    os.system('cls')
    driver.quit()

