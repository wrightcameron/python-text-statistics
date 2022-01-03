import re
import argparse

class TextStatistics:

    wordCount = None
    letterCount = None
    lineCount = None

    wordLengths = None
    wordFrquncy = None

    fileName = None;
    def __init__(self) -> None:
        self.wordCount = 0
        self.letterCount = 0
        self.lineCount = 0
        
        self.wordLengths = {}
        #TODO wordFrequency is misspilled
        self.wordFrquncy = {}
        self.letterFrequency = {}

    def run(self, fileName: str) -> None:
        #TODO Cause this will be used for checking speed should time the takes to finish
        with open(fileName, 'r') as file:
            for line in file:
                self.lineCount += self.countLine(line)
                self.wordCount += self.countWords(line)
                self.letterCount += self.countLetters(line)

                self.countWordLengths(line)
                self.countWordFrequency(line)
                self.countLetterFrequency(line)
        self.results() 

    def countChars(self, line: str) -> int:
        """Count characters in string

        Args:
            line (str): A string

        Returns:
            int: Count of chars in string
        """
        count = 0
        for i, v in enumerate(line):
            count = count + 1
        return count

    def countWords(self, line: str) -> int:
        """Count words in string, anything not containing a-z, A-Z

        Args:
            line (str): A string

        Returns:
            int: Count of words
        """
        match = re.findall('[a-zA-Z]+', line)
        return len(match)

    def countLine(self, line: str) -> int:
        """Count of new lines in string

        Args:
            line (str): A string

        Returns:
            int: Count of new lines in string
        """
        return len(line.split('\n'))
    
    def countLetters(self, line: str) -> int:
        """Count of letters in given string, anything from a-z, A-Z

        Args:
            line (str): A string

        Returns:
            int: Count of letters
        """
        match = re.findall('[a-zA-Z]', line)
        return len(match)

    def countWordLengths(self, line: str) -> int:
        match = re.findall('[a-zA-Z]+', line)
        for word in match:
            wordLen = len(word)
            if wordLen in self.wordLengths:
                self.wordLengths[wordLen] = self.wordLengths[wordLen] + 1
            else:
                self.wordLengths[wordLen] = 0

    def countWordFrequency(self, line: str) -> int:
        match = re.findall('[a-zA-Z]+', line)
        for word in match:
            if word in self.wordFrquncy:
                self.wordFrquncy[word] = self.wordFrquncy[word] + 1
            else:
                self.wordFrquncy[word] = 0

    def countLetterFrequency(self, line: str) -> int:
        match = re.findall('[a-zA-Z]', line)
        for letter in match:
            letter = letter.lower()
            if letter in self.letterFrequency:
                self.letterFrequency[letter] = self.letterFrequency[letter] + 1
            else:
                self.letterFrequency[letter] = 0
    
    def results(self) -> None:
        print("Statistics for {}".format(self.fileName))
        print("==========================================================")
        print("{} lines".format(self.lineCount))
        print("{} words".format(self.wordCount))
        print("{} characters".format(self.letterCount))
        print("------------------------------")
        # Count of each letter
        output = ""
        for k,v in enumerate(self.letterFrequency):
            output += "{} = {}\n".format(k,v)
        print(output)
        print("------------------------------")
        # Length of each word
        print("length frequency")
        print("------ ---------")
        output = ""
        for k,v in enumerate(self.wordLengths):
            output += "{} \t{}\n".format(k,v)
        print(output)
        print("Average word length = {}".format())
        print("==========================================================")
