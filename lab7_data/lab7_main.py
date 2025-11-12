"""
damion ally
lab 7, accessing data in a file
sep 29, 2025
"""

from lab7_function import *

testing()
print("\n---- Example 1: reading file ----")
read_data("phrases.txt")

print("\n---- example 2: reading specific portion of a file ----")
read_up("phrases.txt")

print("\n---- example 3: reading specific portion using readline ----")
read_readline("phrases.txt")

print("\n---- example 4: reading specific portion using readline ----")
read_all("phrases.txt")

print("\n---- example 5: loop through each line ----")
read_each("phrases.txt")

print("\n---- example 6: creating a new file ----")
new_file("Ally.txt")

print("\n---- example 7: append data into an exisitng file ----")
stamp_date("Ally.txt")

print("\n---- EXERCISE ----")
count_yahoo = email_read("user_email.txt", "@yahoo")
count_gmail = email_read("user_email.txt", "@gmail")
count_hotmail = email_read("user_email.txt", "@hotmail")

# Write the counts to reportemail.txt
report = open("reportemail.txt", "w")
report.write(f"gmail = {count_gmail}\n")
report.write(f"yahoo = {count_yahoo}\n")
report.write(f"hotmail = {count_hotmail}\n")
report.close()

print("Report file 'reportemail.txt' has been created successfully!")
