try:
    import traceback
    import os
    import sys
    import numpy
    import scipy
    import matplotlib
    import unittest
    import selenium
    import urllib
    print("All imports achieved successfully")
except ImportError:
    print("A package or module is not installed or doesn't exist. Please ensure all packages are installed."
          " use <python -m pip install 'moduleName'> and relaunch setup.py")
    exit(1)

if __name__ == "__main__":
    # SETUP OF LINKS FOR THE PROJECT FOLDER
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './')))

    # SETUP OF THE LINKS FOR THE CODE FOLDER
    codeFolderNameSetup = input("Enter the name of the folder containing your code:")
    codeFolderNameSetup = "./" + str(codeFolderNameSetup)
    codeFolderPathNameSetup = (os.path.abspath(os.path.join(os.path.dirname(__file__), codeFolderNameSetup)))

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
    testFolderNameSetup = input("Enter the name of the folder containing your tests:")
    testFolderNameSetup = "./" + str(testFolderNameSetup)
    testFolderPathNameSetup = (os.path.abspath(os.path.join(os.path.dirname(__file__), testFolderNameSetup)))

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

