""" 
	----------------------------------
	
	----------------------------------
"""
import random
import string

vowels = 'aelouy'
consonants = 'bcdefghjklmnpqrstvvwxz'
anyletter = string.ascii_lowercase
input_letter_1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:")
input_letter_2 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:")
input_letter_3 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:")

def fn_generator():
	if string.lower(input_letter_1) == 'v':
		letter1 = random.choice(vowels)
	elif string.lower(input_letter_1) == 'c':
		letter1 = random.choice(consonants)
	elif input_letter_1 == 'l'
		letter1 == random.choice(anyletter)
	else:
		letter1 = string.lower(input_letter_1)

	if string.lower(input_letter_2) == 'v':
		letter2 = random.choice(vowels)
	elif string.lower(input_letter_2) == 'c':
		letter2 = random.choice(consonants)
	elif input_letter_2 == 'l'
		letter2 == random.choice(anyletter)
	else:
		letter2 = string.lower(input_letter_2)

	if string.lower(input_letter_3) == 'v':
		letter3 = random.choice(vowels)
	elif string.lower(input_letter_3) == 'c':
		letter3 = random.choice(consonants)
	elif input_letter_3 == 'l'
		letter3 == random.choice(anyletter)
	else:
		letter3 = string.lower(input_letter_3)

	return retrunname

print(fn_generator())
