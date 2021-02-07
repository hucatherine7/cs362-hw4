#Unit testing question 1

import unittest
import question1

class Question1(unittest.TestCase):
    def test_calcVolume(self):
        self.assertEqual(question1.calcVolume(4), 64)
        self.assertEqual(question1.calcVolume(-1), -1)
        self.assertEqual(question1.calcVolume("bad input"), -1)
        # self.assertEqual(question1.calcVolume(-9, -5), -14)
        # self.assertEqual(question1.calcVolume(1.2, -1.3), -0.10000000000000009)



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
