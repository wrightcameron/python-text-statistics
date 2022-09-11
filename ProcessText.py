import argparse
import time

from TextStatistics import TextStatistics

def runTextStatistics(files: list):
    """Run through list of files to get statistic for, loop through all.

    Args:
        files (list): List of all files
    """
    for f in files:
        w = TextStatistics()
        w.run(f)
        print(w)

# Entry point file for running Text Statistics from Command Line
if __name__ == "__main__":
    # Get the filename of text to scan from user, and ask how many times to run text statistics
    parser = argparse.ArgumentParser(description='Get statistics on text.')
    parser.add_argument('fileName', metavar='file', type=str, nargs='+', help='File name to parse')
    parser.add_argument("-t", "--times", help="Run process x number of times", type=int, default=0)
    args = parser.parse_args()

    times = args.times
    print(times)
    # Running it n times, is to see performance
    if times > 0:
        print("Running statistics {} times".format(times))
        for i in range(0, times):
            print("Execution number {}".format(i))
            start = time.time()
            runTextStatistics(args.fileName)
            end = time.time()
            print("The time of execution of TestStatistics is : {:.5f} sec".format(end-start))
    else:
        start = time.time()
        runTextStatistics(args.fileName)
        end = time.time()
        print("The time of execution of TestStatistics is : {:.5f} sec".format(end-start))