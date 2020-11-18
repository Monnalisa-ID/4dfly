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



pl = []
prolist = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all").text
prolist1 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all").text
prolist2 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all").text
dl = []
for i in prolist.splitlines():
    pl.append(i)

for i in prolist1.splitlines():
    pl.append(i)

for i in prolist2.splitlines():
    pl.append(i)

def tri(i):
   try:
    if requests.get(my_url,proxies={"https":"https://"+i},timeout=0.4).status_code == 200:
       print (i)
       tro(i)
   except:
    pass

def fres(i):
    i.refresh()


















opts = Options()
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--allow-running-insecure-content')
opts.add_argument("--proxy-server='direct://'")
opts.add_argument("--proxy-bypass-list=*")
opts.add_argument("--start-maximized")
opts.add_argument('--disable-gpu')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument('--no-sandbox')
opts.add_argument("user-agent=" + user_agent)
opts.add_extension('./buster_ext.crx')
opts.add_argument('--ignore-ssl-erros')
print ('OTW TUYUL BOSQUE....')
driver = webdriver.Chrome(chrome_options=opts)
driver.minimize_window()
driver.get('http://raboninco.com/1sLv9')
path = "/html/body/div[6]/table/tbody/tr[1]/td/div/div[1]/span[2]/a/img"
delay = 10 #Delay
try:
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
