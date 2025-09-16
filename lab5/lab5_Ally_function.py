"""
damion ally
function file
Sep, 15, 2025
lab 5, function
"""
# example 1: define a function that passes two numbers and return the product of it
def product(a=0,b=0):
    c = a*b
    return c

# example 2: function to calculate the hypotenuse
def hypotenuse(side1, side2):
    return (side1**2 + side2**2)**0.5

# example 3: function to check if the number is positive, negative, or zero.
# The function returns a string
def check_number(num):
    if(num>0):
        return "POSITIVE"
    elif (num<0):
        return "NEGATIVE"
    else:
        return "ZERO"
    
    # example 4: function to calculate the average of a list of grades, and return 'true' if the average is greater than 60, otherwise, it returns 'false'

def check_grades(grades):
    # initialize the average grade value
    avg = 0
    # sum the individual 'g' from list 'grades' into 'avg'
    for g in grades:
        avg += g
    # find the average grade
    avg /= len(grades)
    return avg

def check_pass(avg_grade):
    # check if the average is greater than 60
    if avg_grade >= 60:
        return True
    else:
        return False
    
# LAB EXERCISE

<<<<<<< HEAD
import random

GUESS_NUM = 5

def generate_random(min_num, max_num):
    return random.randint(min_num, max_num)
=======
GUESS_NUM = 5

def generate_random(min_num, max_num, seed):
    number = (seed * 73 + 41) % (max_num - min_num + 1)
    return min_num + number
>>>>>>> d9ed3fdf7f22c5cb6b247992540a50187a7d6d49

def compare_number(rand_num):
    if rand_num < GUESS_NUM:
        print("The number is smaller than the guess number")
    elif rand_num > GUESS_NUM:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")