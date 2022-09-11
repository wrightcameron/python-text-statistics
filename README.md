# Python Text Statistics

## Overview

The python text statistics project simply gets statistics based on the imputed text files. This project is simple, so simple its used for teaching computer science in a college 121 class. Why am I redoing a beginner level cs project? Well I am using the text statistics as a base for me to run those functions using multi threading or multi process. I have just wrapped up the text statistics itself so next will be incorporating the multi-threading. This project doesn't need multi-threading, the functions themselves are inefficient due to isolation, but they are isolated to protect against race conditions for eventual threading.

## Requirements

Install:

- Python 3

## Build

TODO: Add any notes on installing correct packages

## Running

When in the repo, use the command.

```bash
python ProcessText.py <textFile>
```

## Testing

### Linting

Python linting uses pylint and flake8.

A general pylint check will use following pylint command

```bash
pylint $(git ls-files '*.py');
```

A general flake8 check will check for everything.  But for continuous integration the command used will be `flake8 . --count --show-source --statistics --exclude flaskEnv/`

```bash
flake8 --exclude flaskEnv/
```

### Unit Testing

Testing is done using unittest; to start testing,

```bash
$ python -m unittest test_TextStatistics.py
```

## Resources

Here are some useful articles that have helped me through this project.

- [RegExr](https://regexr.com/)
- [ArgParse Tutorial](https://docs.python.org/3/howto/argparse.html)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
- [Python socket and selectors: Non-blocking Communication and Timeouts](https://www.demo2s.com/python/python-socket-and-selectors-non-blocking-communication-and-timeouts.html)
- [Netcat in Python](https://www.instructables.com/Netcat-in-Python/)
