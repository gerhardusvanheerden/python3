""" 
	----------------------------------
	2017-03-10
	working copy returning a 3 chat string
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
	if str.lower(input_letter_1) == 'v':
		letter1 = random.choice(vowels)
	elif str.lower(input_letter_1) == 'c':
		letter1 = random.choice(consonants)
	elif str.lower(input_letter_1) == 'l':
		letter1 = random.choice(anyletter)
	else:
		letter1 = str.lower(input_letter_1)

	if str.lower(input_letter_2) == 'v':
		letter2 = random.choice(vowels)
	elif str.lower(input_letter_2) == 'c':
		letter2 = random.choice(consonants)
	elif str.lower(input_letter_2) == 'l':
		letter2 = random.choice(anyletter)
	else:
		letter2 = str.lower(input_letter_2)

	if str.lower(input_letter_3) == 'v':
		letter3 = random.choice(vowels)
	elif str.lower(input_letter_3) == 'c':
		letter3 = random.choice(consonants)
	elif str.lower(input_letter_3) == 'l':
		letter3 = random.choice(anyletter)
	else:
		letter3 = str.lower(input_letter_3)

	return letter1 + letter2 + letter3

#print(fn_generator())

for i in range (20):
	print(fn_generator())
