
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import datetime

class Flipkart:
    def __init__(self):
        options = FirefoxOptions()
        self.folder = 'htmlfiles'
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.url = 'https://www.flipkart.com'

    def create_html(self, html_file):
        fp = open(f'{self.folder}/{html_file}_{datetime.datetime.now():%d%m%y%H%M}.html', 'w')
        wait = ui.WebDriverWait(self.driver, 10) # timeout after 10 seconds
        results = wait.until(lambda driver: self.driver.page_source)
        fp.write(results)

    def get(self,q):
        self.driver.get(f'{self.url}/search?q={q}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
        # https://stackoverflow.com/a/16928204/2351696
        page = 1
        while True:
            next_page = input("Press Enter after Next page click. Press 1 to quit:")
            if next_page=='1': break
        
            self.create_html(page)
            page+=1

if __name__=='__main__':
    scrapper = Flipkart()
    scrapper.get('mobiles')