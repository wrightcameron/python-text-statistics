# Python Text Statistics

## Overview

The python text statistics project simply gets statistics based on the imputed text files. This project is simple, so simple its used for teaching computer science in a college 121 class. Why am I redoing a beginner level cs project? Well I am using the text statistics as a base for me to run those functions using sockets.  The server will be doing the text processing while the client passes the files to be analyzed.  Demonstrating a knowledge of simple sockets in Python.

## Requirements

- Python 3
- pip 3
- poetry

## Build

Project uses Poetry for package management, have Poetry installed `pip install poetry` and run the below command.

```bash
poetry install
```

## Running

When in the repo, use the command. `python ProcessText.py <textFile>`

If wanting to launch the ProcessText server use command, `python server.py -s [host] -p [port]`

When that is running a client can connect with command `python client.py -s [host] -p [port] <file>`

## Testing

### Linting

Python linting uses pylint and flake8.

A general pylint check will use following pylint command `pylint $(git ls-files '*.py');`


A general flake8 check will check for everything.  But for continuous integration the command used will be `flake8 . --count --show-source --statistics --exclude flaskEnv/`

```bash
flake8 --exclude flaskEnv/
```

Linting can also be done with Python Black, `python black <file>`

### Unit Testing

Testing is done using unittest; to start testing,

```bash
poetry shell; \
python -m pytest ./test/
```

## Resources

Here are some useful articles that have helped me through this project.

- [RegExr](https://regexr.com/)
- [ArgParse Tutorial](https://docs.python.org/3/howto/argparse.html)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
- [Python socket and selectors: Non-blocking Communication and Timeouts](https://www.demo2s.com/python/python-socket-and-selectors-non-blocking-communication-and-timeouts.html)
- [Netcat in Python](https://www.instructables.com/Netcat-in-Python/)
