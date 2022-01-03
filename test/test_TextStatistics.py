import unittest
import codecs
import string
import random
import sys

sys.path.append('..')
import TextStatistics

class UnitTestTextStatistics(unittest.TestCase):

    def setUp(self):
        self.wordCounter = TextStatistics.WordCounter()

    def testCountChars(self):
        #Nominal case
        msg = "this line of letters is 32 chars"
        actual = self.wordCounter.countChars(msg)
        self.assertEqual(actual, 32)
        # Empty case
        msg = ""
        actual = self.wordCounter.countChars(msg)
        self.assertEqual(actual, 0)
        # Weird  chars
        msg = "\n\t\t\n"
        actual = self.wordCounter.countChars(msg)
        self.assertEqual(actual, 4)
        #Check multiline
        msg = "this line of letters\nis 32 chars"
        actual = self.wordCounter.countChars(msg)
        self.assertEqual(actual, 32)

    def testCountWords(self):
        msg = "this message has 4 words"
        actual = self.wordCounter.countWords(msg)
        self.assertEqual(actual, 4)
        # Empty Case
        msg = ""
        actual = self.wordCounter.countWords(msg)
        self.assertEqual(actual, 0)
        #No words only numbers and special characters
        msg = "1234 567 89 !@#"
        actual = self.wordCounter.countWords(msg)
        self.assertEqual(actual, 0)
        # Check multiline
        msg = "this\nmessage\nhas\n4\nwords\n"
        actual = self.wordCounter.countWords(msg)
        self.assertEqual(actual, 4)
    
    def testCountLine(self):
        msg = ""
        actual = self.wordCounter.countLine(msg)
        self.assertEqual(actual, 1)
        # Multiple lines from \n
        msg = "\n\n\n"
        actual = self.wordCounter.countLine(msg)
        self.assertEqual(actual, 4)
        # Multiple lines
        msg = """line 1
                line 2"""
        actual = self.wordCounter.countLine(msg)
        self.assertEqual(actual, 2)
    
    def testCountLetters(self):
        msg = "this line has 18 letters"
        actual = self.wordCounter.countLetters(msg)
        self.assertEqual(actual, 18)
        #Empty Case
        msg = ""
        actual = self.wordCounter.countLetters(msg)
        self.assertEqual(actual, 0)
        # Just numbers no letters
        msg = "1234 567 89 !@#"
        actual = self.wordCounter.countLetters(msg)
        self.assertEqual(actual, 0)
        # Multi line
        msg = "this\nline\nhas\n18\nletters"
        actual = self.wordCounter.countLetters(msg)
        self.assertEqual(actual, 18)

    def testCountWordLengths(self):
        pass

if __name__ == '__main__':
    unittest.main()
