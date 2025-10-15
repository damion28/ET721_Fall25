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
    # test with valid input with 3 students and three grades
    @patch('builtins.input', side_effect=['3', '85', '90', '75'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("The class average is 83.33", output)

    # test with invalid number of students and invalid grade value
    @patch('builtins.input', side_effect=['-1', '0', '2', '95', '110', '80'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Number of students must be greater than 0. Please try again", output)
        self.assertIn("Invalid input. Enter a grade between 0 and 100", output)
        self.assertIn("The class average is 87.50", output)

    @patch('builtins.input', side_effect=['Peter', '3', '85', '90', '95'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_num_students_string(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter a positive number", output)
        self.assertIn("The class average is 90.00", output)

    @patch('builtins.input', side_effect=['2', 'Peter', '85', '90'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_grade_string(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid! Enter a numerical value", output)
        self.assertIn("The class average is 87.50", output)


if __name__ == "__main__":
    unittest.main()
