import unittest
import setup

class TestExample(unittest.TestCase):
    def testSetupFunctionsAreImported(self):
    	self.assertTrue(setup.recommendedModulesAreInstalled())
    
    def testSetupFunctionsAreImportedMustUseNameSpace(self):
    	with self.assertRaises(Exception):
	        recommendedModulesAreInstalled()

if __name__ == '__main__':
    unittest.main()

