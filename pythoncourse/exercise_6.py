print("Coding Exercise 6")

import datetime
""" 
	----------------------------------
	2017-03-08
	(1) create new file
	(2) loop thru list of hardcoded files
		(2.1) read each file line by line
		(2.2) append to new file
	(3) close each file that as red
	(4) close new file
	----------------------------------
"""
newfilename = datetime.datetime.now()
filelists = ["file1.txt","file2.txt","file3.txt"]
def consolidatefiles():
	with open(newfilename.strftime("%Y%m%d_%H%M%f") + ".txt", "a") as newfile:
		for onefile in filelists:
			with open(onefile,"r") as onefileopen:
				for line in onefileopen:
					newfile.write(line  + "\n")
			onefileopen.close()
	newfile.close()

consolidatefiles()
