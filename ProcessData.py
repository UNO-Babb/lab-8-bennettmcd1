#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():
    with open("names.dat", 'r') as inFile, open("StudentList.csv", 'w') as outFile:
        outFile.write("Last Name,First Name,UserID,Major-Year\n")
        inFile.readline()

