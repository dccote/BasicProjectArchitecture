# BasicProjectArchitecture
A basic architecture that uses a setup to load up the modules and automatically assures that there are links between the test and the code files. Took me some time, but figured it out. The sys module that is used plays with the PATH of the project interpreter. This is more of a tutorial for myself, but if this can save time to anyone, I would be more than happy with that.

First edit: I upgraded the setup so it is now interactive. I you feel like you could upgrade it again, feel free to do so.

# Easy steps to get going with your(my) project
 	1- clone repository
 	2- run Setup.py
 	3- create your code files and test files
    	4- in your files, do <from setup import *>
 	5- in your test files, don't forget to: <from code import CodeFile>
 	6- reference your functions in your tests like this: <CodeFile.function> or <CodeFile.object>
	
