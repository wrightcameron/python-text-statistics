import argparse
import time

from TextStatistics import TextStatistics

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get statistics on text.')
    parser.add_argument('fileName', metavar='file', type=str, help='File name to parse')
    parser.add_argument("-t", "--times", help="Run process x number of times", action="store_true")
    parser.add_argument("-s", "--single", help="Run process text single threaded", action="store_true")
    parser.add_argument("-m", "--multi", help="Run process text multi threaded", action="store_true")

    args = parser.parse_args()
    
    start = time.time()
    
    w = TextStatistics()
    w.run(args.fileName)

    end = time.time()
    print("The time of execution of TestStatistics is : {} sec".format(end-start))