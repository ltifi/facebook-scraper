import unittest
import app.scrap as scrap


class UneClasseDeTest(unittest.TestCase):

    def test_formatData(self):
        input = '35 likes'
        self.assertEqual(35, scrap.Scrap.format_data(input))


if __name__ == '__main__':
    unittest.main()
