print("Coding Exercise 3")
""" 
	----------------------------------
	2017-02-25
	Exercise 3
	----------------------------------
"""
def convert_celsius_to_fahrenheit(intput_celsius):
	if intput_celsius < -273.15:
		print("celsuis can not be less then -273.15")
	else:
		retrun_fahrenheit = intput_celsius * 9 / 5 + 32
		return retrun_fahrenheit


print(convert_celsius_to_fahrenheit(-420) )

