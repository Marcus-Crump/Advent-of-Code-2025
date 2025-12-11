import unittest
import Day_3_Lobby as d3

class Day_3(unittest.TestCase):
    def test_sample(self):
        expected = 357
        actual = 0
        with open("Day_3_Sample.txt", "r") as file:
            for line in file:
                actual += d3.day_3_p1(line.strip())
        
        try:
            self.assertEqual(expected, actual)
            print("SAMPLE TEST PASSED")
        except AssertionError:
            print(f"TEST FAILED\nAcutal:{actual} != Expected: {expected}")

if __name__ == "__main__":
    unittest.main()