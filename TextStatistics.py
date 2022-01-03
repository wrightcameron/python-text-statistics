import re

class TextStatistics:

    fileName = None;
    def __init__(self) -> None:
        self.wordCount = 0
        self.letterCount = 0
        self.lineCount = 0
        
        self.letterFrequency = {}
        self.wordLengths = {}
        self.wordFrequency = {}
        

    def run(self, fileName: str) -> None:
        with open(fileName, 'r') as file:
            for line in file:
                self.lineCount += self.countLine(line)
                self.wordCount += self.countWords(line)
                self.letterCount += self.countLetters(line)

                self.letterFrequency = self.countLetterFrequency(line, self.letterFrequency)
                self.wordLengths = self.countWordLengths(line, self.wordLengths)
                self.wordFrequency = self.countWordFrequency(line, self.wordFrequency)
                
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

    def countWordLengths(self, line: str, wordLengths: dict = {}) -> int:
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
        sum = 0
        i = 0
        for k, v in self.wordLengths.items():
            sum += k * v
            i += 1 + v
        return sum / i
    
    def results(self) -> None:
        print("Statistics for {}".format(self.fileName))
        print("==========================================================")
        print("{} lines".format(self.lineCount))
        print("{} words".format(self.wordCount))
        print("{} characters".format(self.letterCount))
        print("------------------------------")
        # Count of each letter
        output = ""
        for k,v in self.letterFrequency.items():
            output += "{} = {}\n".format(k,v)
        print(output)
        print("------------------------------")
        # Length of each word
        print("length frequency")
        print("------ ---------")
        output = ""
        for k,v in self.wordLengths.items():
            output += "{} \t{}\n".format(k,v)
        print(output)
        #TODO Format to 1 decimal
        print("Average word length = {}".format(self.avgWordLength))
        print("==========================================================")
