import unittest
from Crypto_Webscraper_Final import Webscraper
from Crypto_Webscraper_Final import 


class WebscraperTestCase(unittest.TestCase):
    def setUp(self):
        selfscraper = Webscraper
        self.scraper.crypto_properties()


    def scroller_check(self):
        actual_i = Webscraper.scroller()
        expected_i = 15
        self.assertEqual(expected_i, actual_i)
        return


    def coin_path_check(self):
        self.assertTrue(isinstance(self.scraper.crypto_properties, dict))
        self.assertTrue(isinstance(self.scraper.crypto_properties["Name"], str))
        #self.assertIn(isinstance(self.scraper.full_coin_list["Price"], '$'))
        self.assertSetEqual(set(self.scraper.crypto_properties.keys()), set(["Price", "Symbol", "Volume", "Market_Cap", "Circulating_Supply"]))


    def test_write_json(self):
        filepath = "/Users/paddy/opt/anaconda3/bin:/Users/paddy/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin"
        self.scraper.save_to_json(filepath)
        self.writtenData = open(filepath, "r").read()
        self.assertEqual(self.writtenData, self.scraper.save_to_json)


if __name__ == '__main__':
    #testing = unittest.TestLoader().loadTestsFromTestCase(WebscraperTestCase)
    unittest.main(verbosity=2)
    