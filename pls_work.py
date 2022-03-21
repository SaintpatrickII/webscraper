from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import uuid
import json
import urllib.request
from selenium.common.exceptions import NoSuchElementException


class Webscraper:
    def __init__(self):
        self.link_list = []
        self.coin_completed = []
        self.driver = webdriver.Chrome('/Users/paddy/Downloads/chromedriver')
        self.driver.get('https://coinmarketcap.com/')
        self.url = 'https://coinmarketcap.com/'
        self.next_page_string = '?page='
        
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cmc-cookie-policy-banner__close"))).click()
        sleep(10)




    def individual_coin_path(self):
        
        sleep(2)
        coin_container = self.driver.find_element_by_xpath('//table[@class="h7vnx2-2 czTsgW cmc-table  "]')
        coin_list = coin_container.find_elements_by_xpath('./tbody/tr')
        return coin_list




    def crypto_properties(self):
        coin_list = self.individual_coin_path()
        self.link_list = []
        sleep(3)
        i = 1
        self.driver.execute_script("window.scrollBy(0, 50)")
        self.driver.execute_script("document.body.style.zoom='50%'")
        print(len(coin_list))
        for i in range(len(coin_list)):
            try:
                full_coin_list= [{
                    'uuid' : str(uuid.uuid4()),
                    'Name': coin_list[i].find_element_by_xpath('.//td[3]//a//p').text,
                    'Symbol' : coin_list[i].find_element_by_xpath('.//td[3]/div/a/div/div/div/p').text,
                    'Price' : coin_list[i].find_element_by_xpath('.//td[4]/div/a/span').text,
                    'Volume' :coin_list[i].find_element_by_xpath('.//td[8]/div/a/p').text,
                    'Market_cap' : coin_list[i].find_element_by_xpath('.//td//p/span[2]').text,
                    'Circulating_Supply' : coin_list[i].find_element_by_xpath('.//td[9]//div/div[1]/p').text
                }]
            except NoSuchElementException:
                    continue
            img = coin_list[i].find_element_by_class_name('coin-logo')
            src = img.get_attribute('src')
            coin_image = urllib.request.urlretrieve(src, "my_image.png" + str(coin_list[i].find_element_by_xpath('.//td[3]//a//p').text))
            #i += 1
            print(full_coin_list)
            coin_list = self.individual_coin_path()
            self.driver.execute_script("window.scrollBy(0, 50)")
            self.link_list.extend(full_coin_list)
            self.coin_completed.extend([coin_image])
            self.save_to_json()
            #self.coin_completed.extend([full_coin_list])
            if i == 100:
                # self.link_list.extend(full_coin_list)
                # self.link_list.extend(coin_image)
                #self.save_to_json()
                return full_coin_list
        # self.driver.execute_script("window.scrollBy(0, 300)")
        #




    #def scroller(self):
        self.driver.execute_script("window.scrollBy(0, 300)")

    def save_to_json(self):
            complete_full_coin_list = self.link_list
            crypto_json = json.dumps(complete_full_coin_list,)
            with open('JSON_pls.json', encoding='utf-8', mode='w') as file:
                json.dump(crypto_json, file, ensure_ascii=False, indent=4)

    #def save_image(self):
        



    def page_iterator(self, no_of_pages):
        sleep(5)
        element = self.driver.find_elements_by_xpath("//a[@aria-label='Next page']")
        page = 1
        while page <= no_of_pages:
            self.crypto_properties()
            self.scroller()
            self.driver.execute_script("document.body.style.zoom='100%'")
            next_page_button = element[1]
            sleep(3)
            next_page_button.click()
            page += 1
            if page == no_of_pages:
                #self.save_to_json()
                return 


if __name__ == '__main__':
    public_webscraper = Webscraper()
    public_webscraper.page_iterator(11)