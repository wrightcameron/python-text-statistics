import unittest
import codecs
import string
import random
import wordCounter

class UnitTestWordCounter(unittest.TestCase):

    def setUp(self) -> None:
        self.wordCounter = wordCounter.WordCounter()

    def testCountLine(self):
        msg = ""
        actual = self.wordCounter.countLine(msg)
        self.assertEqual(actual, 1)
    
    def testCountLetters(self):
        msg = "this line of letters is 26"
        actual = self.wordCounter.countLetters(msg)
        self.assertEqual(actual, 26)

if __name__ == '__main__':
    unittest.main()
