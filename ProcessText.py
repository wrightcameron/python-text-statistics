import argparse

from TextStatistics import TextStatistics

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get statistics on text.')
    parser.add_argument('fileName', metavar='file', type=str, help='File name to parse')
    args = parser.parse_args()
    w = TextStatistics()
    w.run(args.fileName)