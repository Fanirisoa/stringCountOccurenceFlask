#! /usr/bin/python/  python3
# coding: utf-8
import os
import argparse
from sparseArray import *


def parse_arguments():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--queries", action='store', dest='alist',
                    type=str, nargs='*', default=['str1', 'srt2', 'srt3'],
                    help="Examples: -q str1 srt2 srt3")
    
    return parser.parse_args()

    

if __name__ == '__main__':
    varString =  os.environ['MY_STRINGS']
    strings = [i for i in varString.split()]
    args = parse_arguments()
    queries = args.alist
    stringsToQueries =  setStringToCompare(queries,strings)


    print(stringsToQueries.matchingStringsToDic())

