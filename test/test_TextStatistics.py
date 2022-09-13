import pytest
from unittest import TestCase
import sys

sys.path.append("..")
from TextStatistics import TextStatistics


class TestTextStatistics:
    # Given
    # When
    # Then

    @pytest.fixture
    def textStat(self):
        return TextStatistics()

    def test_countChars(self, textStat):
        # Nominal case
        msg = "this line of letters is 32 chars"
        actual = textStat.countChars(msg)
        assert actual == 32
        # Empty case
        msg = ""
        actual = textStat.countChars(msg)
        assert actual == 0
        # Weird  chars
        msg = "\n\t\t\n"
        actual = textStat.countChars(msg)
        assert actual == 4
        # Check multiline
        msg = "this line of letters\nis 32 chars"
        actual = textStat.countChars(msg)
        assert actual == 32

    def test_countWords(self, textStat):
        msg = "this message has 4 words"
        actual = textStat.countWords(msg)
        assert actual == 4
        # Empty Case
        msg = ""
        actual = textStat.countWords(msg)
        assert actual == 0
        # No words only numbers and special characters
        msg = "1234 567 89 !@#"
        actual = textStat.countWords(msg)
        assert actual == 0
        # Check multiline
        msg = "this\nmessage\nhas\n4\nwords\n"
        actual = textStat.countWords(msg)
        assert actual == 4

    def test_countLine(self, textStat):
        msg = ""
        actual = textStat.countLine(msg)
        assert actual == 1
        # Multiple lines from \n
        msg = "\n\n\n"
        actual = textStat.countLine(msg)
        assert actual == 4
        # Multiple lines
        msg = """line 1
                line 2"""
        actual = textStat.countLine(msg)
        assert actual == 2

    def test_countLetters(self, textStat):
        msg = "this line has 18 letters"
        actual = textStat.countLetters(msg)
        assert actual == 18
        # Empty Case
        msg = ""
        actual = textStat.countLetters(msg)
        assert actual == 0
        # Just numbers no letters
        msg = "1234 567 89 !@#"
        actual = textStat.countLetters(msg)
        assert actual == 0
        # Multi line
        msg = "this\nline\nhas\n18\nletters"
        actual = textStat.countLetters(msg)
        assert actual == 18

    def test_countWordLengths(self, textStat):
        msg = "The dog jumped over the dim moon"
        actual = textStat.countWordLengths(msg)
        expected = {3: 4, 4: 2, 6: 1}
        TestCase().assertDictEqual(actual, expected)

    def test_countWordFrequency(self, textStat):
        msg = "Moon moon, dog, less, moon\n dog"
        actual = textStat.countWordFrequency(msg)
        expected = {"moon": 3, "dog": 2, "less": 1}
        TestCase().assertDictEqual(actual, expected)

    def test_countLetterFrequency(self, textStat):
        msg = "Moon moon, dog."
        actual = textStat.countLetterFrequency(msg)
        expected = {"m": 2, "o": 5, "n": 2, "d": 1, "g": 1}
        TestCase().assertDictEqual(actual, expected)

    def test_avgWordLength(self, textStat):
        # Average should be 3.5
        wordLengths = {3: 1, 4: 1}
        textStat.wordLengths = wordLengths
        expected = 3.5
        actual = textStat.avgWordLength
        assert expected == actual
        # Average should be 2.475
        wordLengths = {1: 10, 2: 15, 3: 7, 4: 3, 5: 4, 6: 1}
        textStat.wordLengths = wordLengths
        expected = 2.475
        actual = textStat.avgWordLength
        assert expected == actual
