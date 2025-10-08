"""
damion ally
oct 8, 2025
lab 9, test input and output data
unit test
"""
import unittest
from unittest.mock import patch
import io
import studentsgrade

class TestMainFunction(unittest.TestCase):
    # test with valid input wth 3 students and three grades
    @patch('builtins.input', side_effect = ['3','85','90','75'])
    # capture the printed output
    @patch('sys.stdout', new_callable=io.StringIO)
    
    # define a function to test the input and output
    def test_valid_input(self, mock_stdout, mock_input):
        # call the main function from file 'studentsgrade.py'
        studentsgrade.main()

        # retrive the caputred output
        output = mock_stdout.getvalue()

        # check if the printed output contains the expected average
        self.assertIn("The class average is 83.33", output)

    # TEST WITH INVALID INPUTS, THEN VALID
    @patch('builtins.input', side_effect = ['-1', '0','2','95','110','80'])
    @patch('sys.stdout', new_callable=io.StringIO)

    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Number of students must be greater than 0. Please try again", output)
        self.assertIn("Invalid input. Enter a grade between 0 and 100: ", output)
        self.assertIn("The class average is 87.50", output)

    # EXERCISE: create a unittest for invalid data type, for example when the user input strings


    @patch('bultins.input', side_effect = ['r'])
    @patch('sys.stdout', new_callable=io.StringIO)
    
    def test_invalid_data_type(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid! Enter a numerical value", output)
    
    
# run the unit test automatically
if __name__ == "__main__":
    unittest.main()