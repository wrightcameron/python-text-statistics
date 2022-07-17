import re
import json

class TextStatistics:

    fileName = None;

    def __init__(self) -> None:
        """Constructor for TextStatistics object
        """
        self.wordCount = 0
        self.charCount = 0
        self.letterCount = 0
        self.lineCount = 0
        
        self.letterFrequency = {}
        self.wordLengths = {}
        self.wordFrequency = {}
        

    def collectStatistics(self, text: str) -> None:
        """Instead of opening a file, collect text statistics on text passed in.

        Args:
            text (str): string of words, characters, etc
        """
        self.lineCount += self.countLine(text.strip('\n'))
        self.wordCount += self.countWords(text)
        self.letterCount += self.countLetters(text)
        self.charCount += self.countChars(text)

        self.letterFrequency = self.countLetterFrequency(text, self.letterFrequency)
        self.wordLengths = self.countWordLengths(text, self.wordLengths)
        self.wordFrequency = self.countWordFrequency(text, self.wordFrequency)
    
    def run(self, fileName: str) -> None:
        """Run through all text statistics collected, line by line.  Stores all statistics in global
        variables, then prints those statistics to console.

        Args:
            fileName (str): File name of text
            printResults (bool, optional): [description]. Defaults to True.  Print results of text
            statistics
        """
        with open(fileName, 'r') as file:
            for line in file:
                self.lineCount += self.countLine(line.strip('\n'))
                self.wordCount += self.countWords(line)
                self.letterCount += self.countLetters(line)
                self.charCount += self.countChars(line)

                self.letterFrequency = self.countLetterFrequency(line, self.letterFrequency)
                self.wordLengths = self.countWordLengths(line, self.wordLengths)
                self.wordFrequency = self.countWordFrequency(line, self.wordFrequency)

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

    def countWordLengths(self, line: str, wordLengths: dict = {}) -> int:
        """Count the lengths of words.  Only counts words containing a-z.
        Words containing numbers or special characters are ignored.

        Args:
            line (str): Text/String
            wordLengths (dict, optional): [description]. Defaults to {}.
            If already have a dictionary containing frequency, it can be passed in for efficieny.
            Passing this in would cause a threaded process to not be thread safe.

        Returns:
            int: Dictionary of word lengths and frequency
        """
        match = re.findall('[a-zA-Z]+', line)
        if not match:
            return wordLengths
        for word in match:
            wordLen = len(word)
            if wordLen in wordLengths:
                wordLengths[wordLen] = wordLengths[wordLen] + 1
            else:
                wordLengths[wordLen] = 1
        return wordLengths

    def countWordFrequency(self, line: str, wordFrequency: dict = {}) -> dict:
        """Count the occurancs of words in text.  Only counts words containing 
        a-z.  So words containing numbers or special characters are ignored.

        Args:
            line (str): Text/String
            wordFrequency (dict, optional): [description]. Defaults to {}.
            If already have a dictionary containing frequency, it can be passed in for efficieny.
            Passing this in would cause a threaded process to not be thread safe.

        Returns:
            dict: Dictionary containing word frequency
        """
        match = re.findall('[a-zA-Z]+', line)
        if not match:
            return wordFrequency
        for word in match:
            word = word.lower()
            if word in wordFrequency:
                wordFrequency[word] = wordFrequency[word] + 1
            else:
                wordFrequency[word] = 1
        return wordFrequency

    def countLetterFrequency(self, line: str, letterFrequency: dict = {}) -> dict:
        """Count the occurances of all letters in the text.  Only counts a-z

        Args:
            line (str): Text
            letterFrequency (dict, optional): [description]. Defaults to {}.
            If already have a dictionary containing frequency, it can be passed in for efficieny.
            Passing this in would cause a threaded process to not be thread safe.

        Returns:
            dict: Dictionary containing letter frequency
        """
        match = re.findall('[a-zA-Z]', line)
        if not match:
            return letterFrequency
        for letter in match:
            letter = letter.lower()
            if letter in letterFrequency:
                letterFrequency[letter] = letterFrequency[letter] + 1
            else:
                letterFrequency[letter] = 1
        return letterFrequency

    @property
    def avgWordLength(self) -> int:
        """Get average word length of all words in text, returns
        zero if no words scanned

        Returns:
            int: Average
        """
        if not len(self.wordLengths):
            return 0
        sum = 0
        i = 0
        for k, v in self.wordLengths.items():
            sum += k * v
            i += v
        return sum / i
    
    def returnStatsAsJSON(self) -> str:
        """Instead of returning the results as a string, get statistics as json

        Returns:
            str: JSON string
        """
        output = {}
        output['lineCount'] = self.lineCount
        output['wordCount'] = self.wordCount
        output['letterCount'] = self.letterCount
        output['charCount'] = self.charCount
        #TODO add the rest of the counts
        return json.dumps(output)
        
    def __str__(self):
        """Results of all text statistics done on text

        Returns:
            [type]: String of statistics
        """
        output = f"Statistics for {self.fileName}\n".format(self.fileName)
        output += "==========================================================\n"

        output += f"{self.lineCount} lines\n"
        output += f"{self.wordCount} words\n"
        output += f"{self.letterCount} letters\n"
        output += f"{self.charCount} characters\n"
        output += "------------------------------"
        # Count of each letter
        sortedKeys = sorted(self.letterFrequency)
        for i in sortedKeys:
            output += f"{i} = {self.letterFrequency}\n"
        output += "------------------------------\n"
        # Length of each word
        output += "length frequency\n"
        output += "------ ---------\n"
        sortedKeys = sorted(self.wordLengths)
        for i in sortedKeys:
            output += f"{i} \t{self.wordLengths}\n"
        output += "Average word length = {:.2f}\n".format(self.avgWordLength)
        output += "==========================================================\n"
        return output
