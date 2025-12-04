import unittest
import Day_1_Secret_Entrance as d1

class test_cases(unittest.TestCase):
    def test_1(self):
        input = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
        actual = d1.men(input)
        expected = 6

        try:
            self.assertEqual(actual, expected)
            print("Test 1 Pass")
        except AssertionError:
            print(f"Actual output: {actual} != Expected Output: {expected}")

    def test_2(self):
        input = ["L50","L50","R50","L50","R50","L50","L50","L50","R50","L50"]
        actual = d1.men(input)
        expected = 5

        try:
            self.assertEqual(actual, expected)
            print("Test 2 Pass")
        except AssertionError:
            print(f"Actual output: {actual} != Expected Output: {expected}")

    def test_3(self):
        input = ["L50","L50","R50","L50","R50","L50","L50","L50","R50","L50","R50"]
        actual = d1.men(input)
        expected = 6

        try:
            self.assertEqual(actual, expected)
            print("Test 3 Pass")
        except AssertionError:
            print(f"Actual output: {actual} != Expected Output: {expected}")

    def test_4(self):
        input = ["L50","L100","R200","L300","R400","L500"]
        actual = d1.men(input)
        expected = 6

        try:
            self.assertEqual(actual, expected)
            print("Test 4 Pass")
        except AssertionError:
            print(f"Actual output: {actual} != Expected Output: {expected}")
        
    def test_5(self):
        input = ["L50","L100","R200","L300","R400","L500"]
        actual = d1.man(input)
        expected = 6

        try:
            self.assertEqual(actual, expected)
            print("Test 4 Pass")
        except AssertionError:
            print(f"Actual output: {actual} != Expected Output: {expected}")

if __name__ == "__main__":
    unittest.main()