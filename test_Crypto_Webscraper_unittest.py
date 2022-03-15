import unittest
import Crypto_Webscraper_Final


class WebscraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Crypto_Webscraper_Final.Webscraper()
        self.public_scraper = Crypto_Webscraper_Final.public_Webscraper()


    def testScrollerCheck(self):
        actual_i = Crypto_Webscraper_Final.scroller()
        expected_i = 100
        self.assertEqual(expected_i, actual_i)
        self.assertTrue(isinstance(self.scraper.crypto_properties, dict))
        self.assertTrue(isinstance(self.scraper.crypto_properties["Name"], str))
        self.assertSetEqual(set(self.scraper.crypto_properties.keys()), set(["Price", "Symbol", "Volume", "Market_Cap", "Circulating_Supply"]))
        return

    def testPageIterator(self):
        filepath = "/Users/paddy/opt/anaconda3/bin:/Users/paddy/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin"
        self.public_Wecraper.save_to_json(filepath)
        self.writtenData = open(filepath, "r").read()
        self.assertEqual(self.writtenData, self.scraper.save_to_json)
        return

if __name__ == '__main__':
    #testing = unittest.TestLoader().loadTestsFromTestCase(WebscraperTestCase)
    unittest.main(verbosity=2)
    