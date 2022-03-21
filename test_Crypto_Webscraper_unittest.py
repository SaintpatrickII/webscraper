import unittest
from pls_work import Webscraper



class WebscraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Webscraper()
        
        
    #def test_individualCoinContainer(self):
        actual_container = self.Webscraper.individual_coin_path


    def test_cryptoProperties(self):
        self.assertTrue(isinstance(self.Webscraper.crypto_properties, dict))
        self.assertTrue(isinstance(self.Webscraper.crypto_properties["Name"], str))
        self.assertSetEqual(set(self.Webscraper.crypto_properties.keys()), set(["Price", "Symbol", "Volume", "Market_Cap", "Circulating_Supply"]))
       

    def test_saveToJson(self):
        filepath = "/Users/paddy/opt/anaconda3/bin:/Users/paddy/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin"
        self.public_Webcraper.save_to_json(filepath)
        self.writtenData = open(filepath, "r").read()
        self.assertEqual(self.writtenData, self.Webscraper.save_to_json)

    def test_pageIterator(self):
        actual_i = Webscraper.page_iterator(11)
        expected_i = 11
        self.assertEqual(expected_i, actual_i)

    def tearDown(self):
        Webscraper.quit()
    


if __name__ == '__main__':
    #testing = unittest.TestLoader().loadTestsFromTestCase(WebscraperTestCase)
    unittest.main(verbosity=2)
    