import unittest
import Day_2_Gift_Shop as d2

class TestCases(unittest.TestCase):
    def test_1(self):
        with open("Day_2_Sample.txt", 'r') as file:
            expected = 1227775554
            actual = d2.main(file.readlines()[0].split(sep=","))
            
            try:
                self.assertEqual(actual,expected)
                print("PASSED 1")
            except AssertionError:
                print("Testcase 1 failed")
                print(f"Actual: {actual} != Expected:{expected}")

if __name__ == "__main__":
    unittest.main()