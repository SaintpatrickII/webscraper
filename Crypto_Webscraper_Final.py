from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import uuid
import json
from webdriver_manager.chrome import ChromeDriverManager




class Webscraper:
    def __init__(self):
        self.link_list = []
        self.driver = webdriver.Chrome('/Users/paddy/Downloads/chromedriver')
        self.driver.get('https://coinmarketcap.com/')
        self.url = 'https://coinmarketcap.com/'
        self.next_page_string = '?page='
        
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cmc-cookie-policy-banner__close"))).click()
        sleep(10)
        """
        initiliser:

        sets up empty list for iteration of
        also ensures webdriver is initalised
        and is sent to the correct url
        webpage is left for 2s to ensure all elements have loaded
        """


    

   

    def individual_coin_path(self):
        
        sleep(2)
        coin_container = self.driver.find_element_by_xpath('//table[@class="h7vnx2-2 czTsgW cmc-table  "]')
        coin_list = coin_container.find_elements_by_xpath('./tbody')
        return coin_list

    """
    Individual Coin Path
    
    Selects container which contains every coin's
    details, sorts this into correct tr branch which 
    allows simple for looping of various elements of 
    coins
    """
        
   

    def crypto_properties(self):
        coin_list = self.individual_coin_path()
        self.link_list = []
        sleep(2)
        i= 0

        for coin in coin_list:
            # while i <= 100:
            while (coin.find_elements_by_xpath('./tr//td[3]/div/a/div/div/div/p')) == True:
                    full_coin_list= [{
                        'uuid' : str(uuid.uuid4()),
                        'Name': coin.find_element_by_xpath('.//tr//td[3]//a//p').text,
                        'Symbol' : coin.find_element_by_xpath('.//tr//td[3]/div/a/div/div/div/p').text,
                        'Price' : coin.find_element_by_xpath('.//tr//td[4]/div/a/span').text,
                        'Volume' :coin.find_element_by_xpath('.//tr//td[8]/div/a/p').text,
                        'Market_cap' : coin.find_element_by_xpath('.//tr//td//p/span[2]').text,
                        'Circulating_Supply' : coin.find_element_by_xpath('./tr//td[9]//div/div[1]/p').text
                    }] #for coin in coin_list]
                    i += 1
                    print(coin_list)
                
            else:
                self.driver.execute_script("window.scrollBy(0, 700)")
                sleep(3)
                full_coin_list= [{
                    'uuid' : str(uuid.uuid4()),
                    'Name': coin.find_element_by_xpath('.//tr//td[3]//a//p').text,
                    'Symbol' : coin.find_element_by_xpath('.//tr//td[3]/div/a/div/div/div/p').text,
                    'Price' : coin.find_element_by_xpath('.//tr//td[4]/div/a/span').text,
                    'Volume' :coin.find_element_by_xpath('.//tr//td[8]/div/a/p').text,
                    'Market_cap' : coin.find_element_by_xpath('.//tr//td//p/span[2]').text,
                    'Circulating_Supply' : coin.find_element_by_xpath('./tr//td[9]//div/div[1]/p').text
                }] #for coin in coin_list]
                i += 1
            self.link_list.append(full_coin_list)
            print(full_coin_list)
        return full_coin_list

    """
    Crypto Properties
    
    responsible scraping the various details of each coin
    which is then sorted into dictionary items applicable
    for JSON format
    """
    
    



    def save_to_json(self):
            complete_full_coin_list = Webscraper.crypto_properties(self)
            crypto_json = json.dumps(complete_full_coin_list)
            with open('JSON_test.json', encoding='utf-8', mode='w') as file:
                json.dump(crypto_json, file, ensure_ascii=False, indent=4)

    """
    Save To Json

    Takes scraped coin details &
    saves them to JSON file
    this data can then be utilised
    for analysis & modelling from
    a normalised format
    """



class public_Webscraper(Webscraper):

    def __init__(self):
        super().__init__()
        #full_coin_list = Webscraper.crypto_properties(full_coin_list)
        #public_scraper = Webscraper()
        #self.driver.execute_script("document.body.style.zoom='25%'")
        #Webscraper.individual_coin_path(self)

    # def scroller(self):
    #     #coin_container = Webscraper.individual_coin_path(self)
    #     coin_list = Webscraper.crypto_properties(self)
    #     i = 0
    #     for coin in coin_list:
    #         while (coin.find_element_by_xpath('./tr//td[3]/div/a/div/div/div/p')) == True:
    #             Webscraper.crypto_properties()
    #             i =+ 1
    #             #Webscraper.save_to_json()
    #         else:
    #             self.driver.execute_script("window.scrollBy(0, 700)")
    #             sleep(3)
    #             Webscraper.crypto_properties()
    #             i += 1
    #             print(coin)
    #             #Webscraper.save_to_json()
    #             if i == 100:
    #                 #Webscraper.save_to_json()
    #                 return Webscraper.crypto_properties.full_coin_list()


        """
        Scroller:
        
        Scroller loads entire paage for reliable
        scraping of data, webpage is scrolled top to
        bottom 15 times to ensure every element is 
        loaded before scraping begins
        """
    

    def page_iterator(self, no_of_pages):
        sleep(5)
        element = self.driver.find_elements_by_xpath("//a[@aria-label='Next page']")
        page = 1
        while page <= no_of_pages:
            self.crypto_properties()
            next_page_button = element[1]
            sleep(3)
            next_page_button.click()
            page += 1
            #Webscraper.crypto_properties(self)
            #Webscraper.save_to_json(self)
            if page == no_of_pages:
                 Webscraper.save_to_json(self)
        return 

    """
    Page Iterator
    
    Used to click next page button on the 
    bottom of each webpage, this funcion is 
    iterated 9 times in order to scrape the first
    1000 coins on coinmarketcap.com
    """


private_Webscraper = Webscraper()
coin_public_webscraper = public_Webscraper()
#coin_public_webscraper.page_iterator(11)
#final_coin_list = coin_public_webscraper.scroller()
full_iteration = coin_public_webscraper.page_iterator(10)
coin_public_webscraper.page_iterator(10)
print(full_iteration)
#public_Webscraper.save_to_json(self)
