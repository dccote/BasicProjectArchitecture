import os
import sys

def recommendedModulesAreInstalled():
    try:
        import traceback
        import numpy
        import scipy
        import matplotlib
        import urllib
        import unittest
    except ImportError:
        return False
    return True    

def requestCodeFolder():
    codeFolder = input("Enter the name of the folder containing your code:")
    return codeFolder

def requestTestFolder():
    testFolder = input("Enter the name of the folder containing your tests:")
    return testFolder

def insertAtFrontOfUserPATH(directoryPath):
    sys.path.insert(0, directoryPath)

def removeFromUserPATH(directoryPath):
    sys.path.remove(directoryPath)


if __name__ == "__main__":
    rootFolder = os.path.dirname(__file__)
    codeFolder = 'code' # FIXME: Should pass on argument line
    testFolder = 'tests' # FIXME: Should pass on argument line

    if not codeFolder:
        codeFolder = requestCodeFolder()
    if not testFolder:       
        testFolder = requestTestFolder()

    # SETUP OF THE LINKS FOR THE CODE FOLDER
    codeFolder = "./" + str(codeFolder)
    codeFolderPathNameSetup = (os.path.abspath(os.path.join(os.path.dirname(__file__), codeFolder)))

    if os.path.exists(codeFolderPathNameSetup):
        sys.path.insert(0, codeFolderPathNameSetup)

    else:
        flag_correctAnswerSetup = 0
        while flag_correctAnswerSetup == 0:
            print("folder name specified doesn't exist. Do you want to create it and add it to project PATH?")
            userSetupPathAnswer = input()

            if str(userSetupPathAnswer) == "yes":
                flag_correctAnswerSetup = 1
                os.makedirs(codeFolderPathNameSetup)

                if os.path.exists(codeFolderPathNameSetup):
                    try:
                        sys.path.insert(0, codeFolderPathNameSetup)
                    except Exception:
                        print("An error occurred, please check the file name chosen.")

            elif str(userSetupPathAnswer) == "no":
                flag_correctAnswerSetup = 1
                break

            else:
                print("Command was not recognized. Please enter 'yes' or 'no'.\n")

    # SETUP OF THE LINKS FOR THE TEST FOLDER
    testFolder = "./" + str(testFolder)
    testFolderPathNameSetup = (os.path.abspath(os.path.join(os.path.dirname(__file__), testFolder)))

    if os.path.exists(testFolderPathNameSetup):
        sys.path.insert(0, testFolderPathNameSetup)

    else:
        flag_correctAnswerSetup = 0
        while flag_correctAnswerSetup == 0:
            print("folder name specified doesn't exist. Do you want to create it and add it to project PATH?")
            userSetupPathAnswer = input()

            if str(userSetupPathAnswer) == "yes":
                flag_correctAnswerSetup = 1
                os.makedirs(testFolderPathNameSetup)

                if os.path.exists(testFolderPathNameSetup):
                    try:
                        sys.path.insert(0, testFolderPathNameSetup)
                    except Exception:
                        print("An error occurred, please check the file name chosen.")

            elif str(userSetupPathAnswer) == "no":
                flag_correctAnswerSetup = 1
                break

            else:
                print("Command was not recognized. Please enter 'yes' or 'no'.\n")

    for setupPathName in sys.path:
        if sys.path.count(setupPathName) > 1:
            for i in range(sys.path.count(setupPathName) - 1):
                sys.path.remove(setupPathName)

    print('\n\n================ Project interpreter PATH folders (for modules) ================')
    for setupPathName in sys.path:
        print(setupPathName, sys.path.count(setupPathName))
    print("================================================================================\n\n")



