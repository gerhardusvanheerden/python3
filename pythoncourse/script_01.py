""" 
	----------------------------------
	
	----------------------------------
"""
import random
import string


def fn_generator():
	letter1 = random.choice(string.ascii_lowercase)
	letter2 = random.choice(string.ascii_lowercase)
	letter3 = random.choice(string.ascii_lowercase)
	retrunname = letter1 + letter2 + letter3

	return retrunname

print(fn_generator())
