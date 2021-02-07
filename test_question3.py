#Unit Tests for Question 3

import unittest
import question3

class Question3(unittest.TestCase):
    def test_generateFullName(self):

        #Normal test case
        self.assertEqual(question3.generateFullName("Abe", "Lincoln"), "Abe Lincoln")

        #Test case with wrong type
        self.assertEqual(question3.generateFullName(5, 10), "Bad input")

        #Test case with empty string
        self.assertEqual(question3.generateFullName("John",""), "Bad input")

        #Checks empty list and divide by zero
        # list2 = []
        # self.assertEqual(question3.generateFullName(list2), -1)
        #
        # #Checking float and large test case
        # list3 = [4.2, 5.7, 45.3, 2.1, 1.9, 23.1, 9.9]
        # self.assertEqual(question3.generateFullName(list3), 13.171428571428573)


if __name__ == '__main__':
    unittest.main(verbosity=2)
