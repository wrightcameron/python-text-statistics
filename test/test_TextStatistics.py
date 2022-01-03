import unittest
import sys

sys.path.append('..')
from TextStatistics import TextStatistics

class UnitTestTextStatistics(unittest.TestCase):

    def setUp(self):
        self.testStatistics = TextStatistics()

    def test_countChars(self):
        #Nominal case
        msg = "this line of letters is 32 chars"
        actual = self.testStatistics.countChars(msg)
        self.assertEqual(actual, 32)
        # Empty case
        msg = ""
        actual = self.testStatistics.countChars(msg)
        self.assertEqual(actual, 0)
        # Weird  chars
        msg = "\n\t\t\n"
        actual = self.testStatistics.countChars(msg)
        self.assertEqual(actual, 4)
        #Check multiline
        msg = "this line of letters\nis 32 chars"
        actual = self.testStatistics.countChars(msg)
        self.assertEqual(actual, 32)

    def test_countWords(self):
        msg = "this message has 4 words"
        actual = self.testStatistics.countWords(msg)
        self.assertEqual(actual, 4)
        # Empty Case
        msg = ""
        actual = self.testStatistics.countWords(msg)
        self.assertEqual(actual, 0)
        #No words only numbers and special characters
        msg = "1234 567 89 !@#"
        actual = self.testStatistics.countWords(msg)
        self.assertEqual(actual, 0)
        # Check multiline
        msg = "this\nmessage\nhas\n4\nwords\n"
        actual = self.testStatistics.countWords(msg)
        self.assertEqual(actual, 4)
    
    def test_countLine(self):
        msg = ""
        actual = self.testStatistics.countLine(msg)
        self.assertEqual(actual, 1)
        # Multiple lines from \n
        msg = "\n\n\n"
        actual = self.testStatistics.countLine(msg)
        self.assertEqual(actual, 4)
        # Multiple lines
        msg = """line 1
                line 2"""
        actual = self.testStatistics.countLine(msg)
        self.assertEqual(actual, 2)
    
    def test_countLetters(self):
        msg = "this line has 18 letters"
        actual = self.testStatistics.countLetters(msg)
        self.assertEqual(actual, 18)
        #Empty Case
        msg = ""
        actual = self.testStatistics.countLetters(msg)
        self.assertEqual(actual, 0)
        # Just numbers no letters
        msg = "1234 567 89 !@#"
        actual = self.testStatistics.countLetters(msg)
        self.assertEqual(actual, 0)
        # Multi line
        msg = "this\nline\nhas\n18\nletters"
        actual = self.testStatistics.countLetters(msg)
        self.assertEqual(actual, 18)

    def test_countWordLengths(self):
        msg = "The dog jumped over the dim moon"
        actual = self.testStatistics.countWordLengths(msg)
        expected = {3: 4, 4: 2, 6: 1}
        self.assertDictEqual(actual, expected)

    def test_countWordFrequency(self):
        msg = "Moon moon, dog, less, moon\n dog"
        actual = self.testStatistics.countWordFrequency(msg)
        expected = {"moon": 3, "dog": 2, "less": 1}
        self.assertDictEqual(actual, expected)

    def test_countLetterFrequency(self):
        msg = "Moon moon, dog."
        actual = self.testStatistics.countLetterFrequency(msg)
        expected = {'m': 2, 'o': 5, 'n': 2, 'd':1, 'g':1}
        self.assertDictEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
