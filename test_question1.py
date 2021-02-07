#Unit testing question 1

import unittest
import question1

class Question1(unittest.TestCase):
    def test_calcVolume(self):
        #Normal test case
        self.assertEqual(question1.calcVolume(4), 64)

        #Negative number test case
        self.assertEqual(question1.calcVolume(-1), -1)

        #Wrong input type
        self.assertEqual(question1.calcVolume("bad input"), -1)




if __name__ == '__main__':
    unittest.main(verbosity=2)

#
# import unittest
# from cubeVolume import cubeVolume
#
# class TestCubeVolume(unittest.TestCase):
#
#     def test_cubeVolume(self):
#         self.assertEqual(cubeVolume(3), 27)
#
#     def test_negativeCubeVolume(self):
#         self.assertEqual(cubeVolume(-1), -1)
#
#     def test_nonIntegerCubeVolume(self):
#         self.assertEqual(cubeVolume("string"), -1)
#
# if __name__ == "__main__":
#     unittest.main()
