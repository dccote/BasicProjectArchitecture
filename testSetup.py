import unittest
import setup
import sys
import os
import re

class TestExample(unittest.TestCase):
    def testSetupFunctionsAreImported(self):
    	self.assertTrue(setup.recommendedModulesAreInstalled())
    
    def testSetupFunctionsAreImportedMustUseNameSpace(self):
    	with self.assertRaises(Exception):
	        recommendedModulesAreInstalled()

    # def testPrintPath(self):
    # 	print(sys.path)

    def testWhatIsPath(self):
    	self.assertTrue(sys.path.count != 0)

    def testWhatIsPathElement(self):
    	self.assertTrue(sys.path[0] != '')

    def testRegularExpressionUse(self):
    	self.assertTrue(re.search('dccote', '/Users/dccote'))

    def testUsernameIsFirstElement(self):
     	username = os.environ['USER']
     	self.assertTrue(username)
     	self.assertTrue(re.search(username, sys.path[0]))

    def testInsertIntoPathManually(self):
    	savePath = sys.path[:] # Copy elements, not reference
    	somePath = '/tmp/blabla'
    	sys.path.insert(0,somePath)
    	self.assertEqual(sys.path[0], somePath)
    	self.assertNotEqual(savePath, sys.path)
    	sys.path.remove(somePath)
    	self.assertEqual(savePath, sys.path)

    def testInsertIntoPath(self):
    	savePath = sys.path[:] # Copy elements, not reference
    	somePath = '/tmp/blabla'
    	setup.insertAtFrontOfUserPATH(somePath)
    	self.assertEqual(sys.path[0], somePath)
    	self.assertNotEqual(savePath, sys.path)
    	setup.removeFromUserPATH(somePath)
    	self.assertEqual(savePath, sys.path)

if __name__ == '__main__':
    unittest.main()

