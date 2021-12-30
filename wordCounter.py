
class wordCounter:

    wordCount = None
    letterCount = None
    wordFrquncy = None
    lineCount = None

    fileName = None;
    def __init__(self) -> None:
        self.wordCount = 0
        self.letterCount = 0
        self.lineCount = 0
        self.wordFrquncy = {}

    def run(self, fileName: str) -> None:
        #TODO Cause this will be used for checking speed should time the takes to finish
        with open(fileName, 'r') as file:
            for line in file:
                self.wordCount += self.countWords(line)
                self.letterCount += self.countLetters(line)
                self.lineCount += self.countLine(line)
        self.results() 

    def countLine(self, line: str) -> int:
        return 1
    
    def countWords(self, line: str) -> int:
        #TODO Need to remove non word characters
        count = 0
        for word in line:
            count = count + 1
        return count

    def countLetters(self, line: str) -> int:
        #TODO Need to remove non word characters
        count = 0
        for i, v in enumerate(line):
            count = count + 1
        return count
    def results(self) -> None:
        print("Results from scanning {}".format(self.fileName))
        print("The number of words: {}".format(self.wordCount))
        print("The number of letters: {}".format(self.letterCount))
        print("The number of lines: {}".format(self.lineCount))
    #TODO Count number of words
    #TODO Count number of letters
    #TODO Count frequency of words
    #TODO Count number of lines
    #TODO Print this all outl

if __name__ == "__main__":
    w = wordCounter()
    w.run('./greatGatsby.txt')
