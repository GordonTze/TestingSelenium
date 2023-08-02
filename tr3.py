from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import threading

global count
def loop(df_url, driver):
    global count
    while True:

        website_random_URL = random.sample(df_url.url.to_list(), 1)

        driver.get(website_random_URL[0])
        time.sleep(2)
        height = int(driver.execute_script("return document.documentElement.scrollHeight"))

        
        driver.execute_script('window.scrollBy(0,10)')
        time.sleep(0.10)
        totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
        count += 1
        print('***Web Page Visited {} times***'.format(count))

def main():
    global count
    count = 0
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver_path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(service = Service(driver_path), options = options)
    #driver.maximize_window()
    col_name = ['url']
    df_url = pd.read_csv("links.txt", names=col_name)

    # create threads
    t1 = threading.Thread(target = loop, args = (df_url, driver))
    t2 = threading.Thread(target = loop, args = (df_url, driver))
    t3 = threading.Thread(target = loop, args = (df_url, driver))

    print('starting thread 1')
    t1.start()
    time.sleep(1)

    print('starting thread 2')
    t2.start()
    time.sleep(1)

    print('starting thread 3')
    t3.start()

    # wait for thread to end
    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
