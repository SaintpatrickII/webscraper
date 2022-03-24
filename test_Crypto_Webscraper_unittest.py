import unittest
from Crypto_Webscraper import Webscraper
import json
from selenium import webdriver


class WebscraperTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/paddy/Downloads/chromedriver')
        self.driver.get('https://coinmarketcap.com/')
        self.coin_path = Webscraper.individual_coin_path(self)
        self.scraper_properties = Webscraper.crypto_properties(self)
        with open('/Users/paddy/Desktop/AiCore/Scraper_Project/coins.json', mode='r') as f:
            self.coins_json = json.load(f)
        
        
    
        # self.assertTrue(isinstance(self.scraper.crypto_properties["Name"], str))

    #def test_individualCoinContainer(self):
        #actual_container = self.Webscraper.individual_coin_path


    def test_coin_path(self):
        self.coin_path()

    def testCryptoProperties(self):
        self.assertTrue(isinstance(self.scraper_properties, list))
        # self.assertTrue(isinstance(self.scraper.crypto_properties["Name"], str))
        # self.assertSetEqual(set(self.scraper.crypto_properties.keys()), set(["uuid", "name", "Symbol", "Price",  "Volume", "Market_Cap", "Circulating_Supply"]))
    #    #is list, is each element dict


    def test_is_json_list(self):
        self.assertIsInstance(self.coins_json, list)

    
    # #def testSaveToJson(self):
    #     # filepath = "/Users/paddy/opt/anaconda3/bin:/Users/paddy/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin"
    #     # self.scraper.save_to_json()
    #     # self.writtenData = open(filepath, "a").read()
    #     # self.assertEqual(self.writtenData, self.scraper.save_to_json)

    # def testPageIterator(self):
    #     actual_i = self.scraper.page_iterator(11)
    #     expected_i = type(None)
    #     #test NoneType
    #     self.assertEqual(expected_i, actual_i)

    def tearDown(self):
        pass
    #     self.scraper.quit()
    


if __name__ == '__main__':
    #testing = unittest.TestLoader().loadTestsFromTestCase(WebscraperTestCase)
    unittest.main(verbosity=2)
    

