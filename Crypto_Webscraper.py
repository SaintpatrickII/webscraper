from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import uuid
import json
# import urllib.request
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
import boto3
import logging
# from botocore.exceptions import ClientError
import os

class Webscraper:
    def __init__(self):
        self.link_list = []
        self.coin_image_completed = []
        #self.image_srs_list = []
        self.driver = webdriver.Chrome('/Users/paddy/Downloads/chromedriver')
        self.driver.get('https://coinmarketcap.com/')
        self.url = 'https://coinmarketcap.com/'
        self.next_page_string = '?page='
        
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cmc-cookie-policy-banner__close"))).click()
        sleep(10)

    """
    Initaliser:
    
    defines driver local location, creates
    empty lists to be used in webscraper &
    defines website to be webscraped, also
    clicks cookie banner
    """
    
    
    def individual_coin_path(self):
        
        sleep(2)
        coin_container = self.driver.find_element_by_xpath('//table[@class="h7vnx2-2 czTsgW cmc-table  "]')
        coin_list = coin_container.find_elements_by_xpath('./tbody/tr')
        return coin_list

    
    """
    Individual_coin_path:
    
    defines table on webpage which is
    to be iterated through to scrape 
    properties of various coins
    """


    def crypto_properties(self):
        coin_list = self.individual_coin_path()
        self.image_path = '/Users/paddy/Desktop/AiCore/Scraper_Project/Coin_Images'
        sleep(3)
        i = 1
        self.driver.execute_script("window.scrollBy(0, 50)")
        self.driver.execute_script("document.body.style.zoom='50%'")
        for i in range(len(coin_list)):
            try:
                full_coin_list= {
                    'uuid' : str(uuid.uuid4()),
                    'Name': coin_list[i].find_element_by_xpath('.//td[3]//a//p').text,
                    'Symbol' : coin_list[i].find_element_by_xpath('.//td[3]/div/a/div/div/div/p').text,
                    'Price' : coin_list[i].find_element_by_xpath('.//td[4]/div/a/span').text,
                    'Volume' :coin_list[i].find_element_by_xpath('.//td[8]/div/a/p').text,
                    'Market_cap' : coin_list[i].find_element_by_xpath('.//td//p/span[2]').text,
                    'Circulating_Supply' : coin_list[i].find_element_by_xpath('.//td[9]//div/div[1]/p').text
                }
                img = coin_list[i].find_element_by_class_name('coin-logo')
                full_image_list = {
                        'uuid' : str(uuid.uuid4()),
                        'Name': coin_list[i].find_element_by_xpath('.//td[3]//a//p').text,
                        'Image' : img.get_attribute('src')
                        }
            except NoSuchElementException:
                    continue
            if coin_list[i] in full_coin_list.values():
                continue
            
                coin_list = self.individual_coin_path()
            # img = coin_list[i].find_element_by_class_name('coin-logo')
            # # for image in img:
            # src = img.get_attribute('src')
            # #     self.image_srs_list.append(image.get_attribute('src'))
            # coin_image = urllib.request.urlretrieve(src, '/Users/paddy/Desktop/AiCore/Scraper_Project/Coin_Images/' + str(coin_list[i].find_element_by_xpath('.//td[3]/div/a/div/div/div/p').text) + ".png")
            #self.save_image_url()
            print(full_coin_list)
            #print(self.image_srs_list)
            self.link_list.append(full_coin_list)
            coin_list = self.individual_coin_path()
            #image_scraper = self.save_image_url()
            
            self.driver.execute_script("window.scrollBy(0, 50)")
            self.save_to_json()
            self.save_to_json_image()
            self.coin_image_completed.append(full_image_list)
            # self.image_srs_list.append
            if i == 100:
                #self.save_to_json()
                return full_coin_list()


    """
    crypto_properties:
    
    main bulk of webscraper, this scrapes
    all items from each coin i.e. images &
    attributes alongside scrolling the 
    webscraper to the bottom of each page
    """


    def save_to_json(self):
        final_coin_list = []
        for coin in self.link_list:
            if coin not in final_coin_list:
                final_coin_list.append(coin)
        
        complete_full_coin_list = final_coin_list
        # crypto_json = json.dump(complete_full_coin_list)
        with open('coins.json', encoding='utf-8', mode='w') as file:
            json.dump(complete_full_coin_list, file, ensure_ascii=False, indent=4)


        
    



    def save_to_json_image(self):
        final_image_list = []
        for coin in self.coin_image_completed:
            if coin not in final_image_list:
                final_image_list.append(coin)
        
        complete_full_image_list = final_image_list
        # crypto_json_image = json.dumps(complete_full_coin_list)
        with open('coins_images.json', encoding='utf-8', mode='w') as file:
            json.dump(complete_full_image_list, file, ensure_ascii=False, indent=4)


    """
    save_to_json:
    
    responsible for ensuring no duplicate 
    results saved & all coins saved to
    easy to read json format
    """


    def page_iterator(self, no_of_pages):
        sleep(5)
        element = self.driver.find_elements_by_xpath("//a[@aria-label='Next page']")
        page = 1
        while page <= no_of_pages:
            self.crypto_properties()
            self.driver.execute_script("document.body.style.zoom='100%'")
            next_page_button = element[1]
            sleep(3)
            next_page_button.click()
            page += 1
            if page == no_of_pages:
                self.save_to_json()
                return 


    """
    page_iterator:
    
    responsible for iterating
    webscraper through first 10
    pages of website, alongside 
    saving results once webscraper 
    finishes
    
    input: no_of_pages = int
    """


   


if __name__ == '__main__':
    public_webscraper = Webscraper()
    public_webscraper.page_iterator(11)


