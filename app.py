#! /usr/bin/python/  python3
# coding: utf-8
from flask import Flask
import os
import argparse
from sparseArray import *


app = Flask(__name__)

def parse_arguments():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--queries", action='store', dest='alist',
                    type=str, nargs='*', default=['str1', 'srt2', 'srt3'],
                    help="Examples: -q str1 srt2 srt3")
    
    return parser.parse_args()

@app.route('/')
def index():
    return print(stringsToQueries.matchingStringsToDic())

if __name__ == "__main__":
    varString =  os.environ['MY_STRINGS']
    strings = [i for i in varString.split()]
    args = parse_arguments()
    queries = args.alist
    stringsToQueries =  setStringToCompare(queries,strings)
    app.run(debug = True)