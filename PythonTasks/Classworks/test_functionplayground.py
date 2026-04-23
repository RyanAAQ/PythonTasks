import unittest
import functionplayground


class TestCubeFunction(unittest.TestCase):

    def test_that_cube_function_exists(self):
        functionplayground.cube(3)
        
    def test_that_cube_function_returns_correct_result(self):
        actual = functionplayground.cube(3)
        expected = 27
        self.assertEqual(actual, expected)


    def test_that_cube_function_return_invalid_data_type_with_wrong_input(self):
        actual = functionplayground.cube("musa")
        expected = "invalid input"
        self.assertEqual(actual, expected)
