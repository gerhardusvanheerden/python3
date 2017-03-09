""" 
	----------------------------------
	
	----------------------------------
"""
import random
import string

vowels = 'aelouy'
consonants = 'bcdefghjklmnpqrstvvwxz'

input_letter_1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:")
input_letter_2 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:")
input_letter_3 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:")

def fn_generator():
	if string.lower(input_letter_1) == 'v':
		letter1 = random.choice(vowels)
	elif string.lower(input_letter_1) == 'c':
		letter1 = random.choice(consonants)
	elif input_letter_1 == 'l'
		letter1 == input_letter_1

	return retrunname

print(fn_generator())
