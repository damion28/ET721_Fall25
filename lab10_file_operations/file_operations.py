"""
Damion Ally
10/17/2025
lab 10
"""


def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)


def read_file(filename):
    with open(filename, "r") as file:
        file.readlines()


def append_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added.")


# funtion from exercise lab 7 (yesterday)


def email_read(filename, email):
    count_email = 0
    try:
        with open(filename, "r") as file1:
            filelines = file1.readlines()

            for eachline in filelines:
                if email in eachline:
                    count_email += 1

        return count_email

    except FileNotFoundError:
        print("File not found. Please check the filename.")
        return 0
