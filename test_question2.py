#Unit tests for question 2

import unittest
import question2

class Question2(unittest.TestCase):
    def test_findAverage(self):

        #Normal test case
        list1 = [4, 6, 8, 15, 12, 15]
        self.assertEqual(question2.findAverage(list1), 10)

        #Checks empty list and divide by zero
        list2 = []
        self.assertEqual(question2.findAverage(list2), -1)

        #Checking float and large test case
        list3 = [4.2, 5.7, 45.3, 2.1, 1.9, 23.1, 9.9]
        self.assertEqual(question2.findAverage(list3), 13.171428571428573)


if __name__ == '__main__':
    unittest.main(verbosity=2)
