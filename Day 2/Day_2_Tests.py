import unittest
import Day_2_Gift_Shop as d2

class TestCases(unittest.TestCase):
    def test_1(self):
        with open("Day_2_Sample.txt", 'r') as file:
            expected = 1227775554
            actual = d2.day_1(file.readlines()[0].split(sep=","))
            
            try:
                self.assertEqual(actual,expected)
                print("PASSED 1")
            except AssertionError:
                print("Testcase 1 failed")
                print(f"Actual: {actual} != Expected:{expected}")
    def test_sliding_0(self):
        num = 111111111
        try:
            self.assertTrue(d2.is_invalid_pt2(num))
            print("PASSED SLIDE TEST 0")
        except AssertionError:
            print("Slide test 0 did not work")
        
    def test_sliding_1(self):
        num = 12121212
        try:
            self.assertTrue(d2.is_invalid_pt2(num))
            print("PASSED SLIDE TEST 1")
        except AssertionError:
            print("Slide test 1 did not work")
    def test_sliding_2(self):
        num = 123123123
        try:
            self.assertTrue(d2.is_invalid_pt2(num))
            print("PASSED SLIDE TEST 2")
        except AssertionError:
            print("Slide test 2 did not work")
    def test_sliding_3(self):
        num = 12341234
        try:
            self.assertTrue(d2.is_invalid_pt2(num))
            print("PASSED SLIDE TEST 3")
        except AssertionError:
            print("Slide test 3 did not work")
    def test_sliding_4(self):
        num = 1234512345
        try:
            self.assertTrue(d2.is_invalid_pt2(num))
            print("PASSED SLIDE TEST 4")
        except AssertionError:
            print("Slide test 4 did not work")
    def test_part_2(self):
        with open("Day_2_Sample.txt", 'r') as file:
            expected = 4174379265
            actual = d2.main(file.readlines()[0].split(sep=","))
            
            try:
                self.assertEqual(actual,expected)
                print("PASSED DAY 2 SAMPLE")
            except AssertionError:
                print("Day 2 testcase 1 failed")
                print(f"Actual: {actual} != Expected:{expected}")

if __name__ == "__main__":
    unittest.main()