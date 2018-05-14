# Basic test for example
import unittest
from code import exemple


class TestExample(unittest.TestCase):
    def testAdd(self):
        self.assertTrue(exemple.add(5, 4) == 9, "Addition doesn't work")

