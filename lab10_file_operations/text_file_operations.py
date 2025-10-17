"""
Damion Ally
10/17/2025
lab 10
"""
import unittest
import os
from file_operations import read_file, write_file, append_file, email_read

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temporary test file name before each test
        self.filename = "test_file.txt"

    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)
    
    def test_write_file(self):
        # test writing text to a file
        msg = "Damion Ally"
        with open(self.filename, "w") as f:
            f.write(msg)

        # verify file exits and content matches
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()

        self.assertEqual(result,msg)

    def test_read_file(self):
        # test reading text from a file
        expected_content = "Read me!"
        with open(self.filename, "w") as f:
            f.write(expected_content)

        with open(self.filename, "r") as f:
            data = f.read()

        self.assertEqual(data, expected_content)

    def test_append_file(self):
        initial_content = "Line one"
        append_content = "\nLine two"

        # Create and write initial content
        with open(self.filename, "w") as f:
            f.write(initial_content)

        # Append new content
        with open(self.filename, "a") as f:
            f.write(append_content)

        # Read the final result
        with open(self.filename, "r") as f:
            final_data = f.read()

        self.assertEqual(final_data, initial_content + append_content)

    # LAB EXERCISE
    def test_email_read(self):
        # Create a sample file to test
        test_content = """john@gmail.com
            sarah@yahoo.com
            peter@hotmail.com
            anna@gmail.com
            lucas@yahoo.com
            """

        with open(self.filename, "w") as f:
            f.write(test_content)

        # Test gmail count
        gmail_count = email_read(self.filename, "@gmail")
        self.assertEqual(gmail_count, 2)

        # Test yahoo count
        yahoo_count = email_read(self.filename, "@yahoo")
        self.assertEqual(yahoo_count, 2)

        # Test hotmail count
        hotmail_count = email_read(self.filename, "@hotmail")
        self.assertEqual(hotmail_count, 1)

        # Ensure no error occurs when reading a valid file
        self.assertIsInstance(gmail_count, int)
            
# run the unit tests automatically when the file is run
if __name__ == "__main__":
    unittest.main()