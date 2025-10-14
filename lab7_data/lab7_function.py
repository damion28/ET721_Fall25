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

# EXAMPLE 2:


# EXAMPLE 3:


# EXAMPLE 4:


# EXAMPLE 5: loop through a readlines file
def read_each(filename):
    with open(filename, "r") as file1:
        filelines = file1.readlines()

        # loop through each item in 'filelines'
        for eachline in filelines:
            print(eachline.strip())
            # strip() removes the newline character \n

# EXAMPLE 6: create a new file
def new_file(filename):
    with open(filename, "w") as file:
        file.write("Python Basics for data analysis")
        file.write("Damion Ally")

# EXAMPLE 7: append data into an existing file
from datetime import datetime

def stamp_date(filename):
    with open(filename, "a") as file:
        file.write(f"\n\n{datetime.now()}")

# EXERCISE
def email_read(filename, email):
    count_email = 0
    with open(filename, "r") as file1:
        filelines = file1.realines()
        # loop through each item in 'filelines'
        for eachline in filelines:
            print(eachline.strip())
            if # complete the statement
                # code to increase the count_email
                return count_email