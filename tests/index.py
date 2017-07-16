import unittest

from selenium import webdriver


class Index(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_open_index_page(self):
        driver = self.driver
        driver.get("https://www.butik.ru/")
        self.assertIn("Бутик.ру", driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
