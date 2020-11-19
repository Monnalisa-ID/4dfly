#Ver 1.25 UPDATE
#Created By Monnalisa-ID
#Do Creative Don't Recode :D
import time,sys,random,os
import datetime
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
texto = "BOT ADFLY \nMade BY Monnalisa"
print(texto.center(60,"+"))
print("_"*60)
ua = UserAgent()
a = ua.random
user_agent = ua.random
print (user_agent)
proxcrot = requests.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt").text
proxme = open(str('proxy.txt'), 'w+')
print('Scraping Proxy...')
time.sleep(5)
print('Creating File Proxy...')
time.sleep(3)
proxy = proxme.read()
xxx = "\n{}".format(proxcrot)
proxme.write(xxx)
proxme.close()



myProxy = random.choice(open('proxy.txt').readlines())
parts = myProxy.strip().split(":") # strip removes spaces and line breaks
host = parts[0]
port = int(parts[1]) # port needs to be an integer


my_url = 'http://raboninco.com/1sLv9'
def fres(i):
    i.refresh()




opts = Options()
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--allow-running-insecure-content')
#opts.add_argument("--proxy-server='direct://'")
#opts.add_argument("--proxy-bypass-list=*")
opts.add_argument('--proxy-server=%s' % myProxy)
print('Selesai Scraping Proxy')
time.sleep(3)
print('MOHON TUNGGU SEBENTAR...')
time.sleep(5) 
print(port)
opts.add_argument("--start-maximized")
opts.add_argument('--disable-gpu')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument('--no-sandbox')
opts.add_argument("user-agent=" + user_agent)
opts.add_extension('./buster_ext.crx')
opts.add_argument('--ignore-ssl-erros')
print ('OTW TUYUL BOSQUE....')
driver = webdriver.Chrome(chrome_options=opts)
driver.get(my_url)
driver.minimize_window()
path = "/html/body/div[6]/table/tbody/tr[1]/td/div/div[1]/span[2]/a/img"
delay = 15 #Delay

try:
        driver.get(my_url)
        element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, path)))
        element.click()
        os.system('cls')
        print ('OTW MENUYUL BOSQUE....')
        time.sleep(2)
finally:
        print('MISI SELESAI BOSQUE...')
        time.sleep(3)
        os.system('cls')
        driver.quit()

tp = ThreadPool(5000)
tp.map(tri,pl)
tp = ThreadPool(300)
tp.map(fres,dl)
