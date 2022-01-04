# Python Text Statistics 
* Author: Cameron Wright

## Overview

The python text statistics project simply gets statistics based on the imputed text files. This project is simple, so simple its used for teaching computer science in a college 121 class. Why am I redoing a beginner level cs project? Well I am using the text statistics as a base for me to run those functions using multi threading or muli process. I have just wrapped up the text statistics itself so next will be incorporating the multi threading. This project doesn't need multi threading, the functions themselves are inefficient due to isolation, but they are isolated to project race stack variables for eventual threading. 
 
## Usage

Pull down the repository, you will need atleast python 3 to run code.  When in the repo, use the command.
```bash
$ python python ProcessText.py <textFile>
```

Unit Testing is done using the python unittest package.  To run the tests, from the tests dir use the following command.
```bash
$ python -m unittest test_TextStatistics.py
```

## Discussion
TODO


## Helpful Resources
TODO