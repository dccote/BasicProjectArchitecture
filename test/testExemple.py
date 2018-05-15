# Basic test for example
from setup import *
from code import exemple


class TestExample(unittest.TestCase):
    def testAdd(self):
        self.assertTrue(exemple.add(5, 4) == 9, "Addition doesn't work")

