import os
import sys
import unittest


class TestSetup(unittest.TestCase):

    def testWriteInPATH(self):
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './code')))
        print("\n\n================ Project interpreter PATH folders (for modules) ================")
        for PathName in sys.path:
            print(PathName)
        print("================================================================================\n\n")
        self.assertIn(str(os.path.abspath(os.path.join(os.path.dirname(__file__), './code'))), sys.path,
                      "The path containing the code files was not added.")

    def testPathExists(self):
        self.assertTrue(os.path.exists(str(os.path.abspath(os.path.join(os.path.dirname(__file__), './code')))),
                        "Path does not exist, please name your folder containing the code, 'code'")


if __name__ == '__main__':
    unittest.main()
