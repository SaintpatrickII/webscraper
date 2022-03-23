
import unittest
from Crypto_Webscraper import Webscraper



class WebscraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Webscraper()
        
        
    #def test_individualCoinContainer(self):
        #actual_container = self.Webscraper.individual_coin_path


    def testCryptoProperties(self):
        self.assertTrue(isinstance(self.scraper.crypto_properties, list))
        # self.assertTrue(isinstance(self.scraper.crypto_properties["Name"], str))
        # self.assertSetEqual(set(self.scraper.crypto_properties.keys()), set(["uuid", "name", "Symbol", "Price",  "Volume", "Market_Cap", "Circulating_Supply"]))
       #is list, is each element dict

    #def testSaveToJson(self):
        # filepath = "/Users/paddy/opt/anaconda3/bin:/Users/paddy/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin"
        # self.scraper.save_to_json()
        # self.writtenData = open(filepath, "a").read()
        # self.assertEqual(self.writtenData, self.scraper.save_to_json)

    def testPageIterator(self):
        actual_i = self.scraper.page_iterator(11)
        expected_i = type(None)
        #test NoneType
        self.assertEqual(expected_i, actual_i)

    def tearDown(self):
        self.scraper.quit()
    


if __name__ == '__main__':
    #testing = unittest.TestLoader().loadTestsFromTestCase(WebscraperTestCase)
    unittest.main(verbosity=2)
    

