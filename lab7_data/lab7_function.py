"""
damion ally
lab 7, accessing data in a file (function)
sep 29, 2025
"""
def testing():
    print("damion ally")

# EXAMPLE 1: read file
def read_data(filename):
    # pipe a text line in a file with a Python code
    fileuser = open(filename, 'r')

    # use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)