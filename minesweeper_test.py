import unittest
import os
from group_minesweeper import read_input, count_mines, process_fields, generate_file

class TestMinesweeper(unittest.TestCase):

    def setUp(self):
        """
        unittest framework method to set up a fresh input and output file for test cases to use
        """
        self.test_input_file = 'test_input.txt'
        self.test_output_file = 'test_output.txt'
        with open(self.test_input_file, 'w') as file:
            file.write("4 4\n*...\n....\n.*..\n....\n0 0\n")

    def tearDown(self):
        """
        unit test framework method to delete input and output file after completing a test case
        """
        os.remove(self.test_input_file)
        if os.path.exists(self.test_output_file):
            os.remove(self.test_output_file)

    def test_read_input(self):
        """
        test that we correctly read and process input data from a file
        """
        expected = [['*...', '....', '.*..', '....']]
        result = read_input(self.test_input_file)
        self.assertEqual(result, expected)

    def test_count_mines(self):
        """
        test that we count the correct number of mines around a specified cell
        """
        field = ['*...', '....', '.*..', '....']
        self.assertEqual(count_mines(field, 0, 1), 1)
        self.assertEqual(count_mines(field, 2, 2), 1)
        self.assertEqual(count_mines(field, 1, 1), 2)

    def test_process_fields(self):
        """
        test that field types are processed correctly and generate the correct mine count
        """

        inputs = [['*...', '....', '.*..', '....']]
        expected = ["Field #1:\n*100\n2210\n1*10\n1110"]
        result = process_fields(inputs)
        self.assertEqual(result, expected)

    def test_generate_file(self):
        """
        test that processed minefield data is written to the output file
        """
        file_outputs = ["Field #1:\n*100\n2210\n1*10\n1110"]
        generate_file(self.test_output_file, file_outputs)
        with open(self.test_output_file, 'r') as file:
            content = file.read().strip()
        self.assertEqual(content, file_outputs[0])


if __name__ == '__main__':
    unittest.main()
