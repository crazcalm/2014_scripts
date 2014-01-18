""" I need to fix this!!!

User choose:
	1. length of password
	2. option to use special characters in password
"""

import random, string

def password_length(pass_len = 0): # need to test
	
	limit = 1000

	print "Please enter the desired length for your password."
	print "The length must be an integer greater than 5."
	pass_len = raw_input("Enter length here: ").strip()
	

	if not pass_len.isdigit():
		print "I do not understand that input.\n"
		password_length()

	else:
		pass_len = int(pass_len)

	if pass_len <= 5:
		print "That  number is to small.\nTry again\n"
		password_length()

	elif pass_len >= limit:
		print "Our password length limit is %s." % (limit)
		print "Sorry\n"
		password_length()

	return pass_len
	

def useable_chars(sample_set = string.printable[:62]):
	
	print "Do you want to use special characters in your password?"
	user = raw_input("Y/N\n").strip()
	
	# Need an isinstance to confirm string
	while not user.lower() == "y" and not user.lower() == "n":
		print "I do not understand.\nTry again"
		useable_chars()

	if user.lower() == "y":
		sample_set = string.printable[:-6]

	else:
		sample_set = string.printable[:62]

	return sample_set

# Need to create "choose the number of digits function"
def num_of_digits(num = 0):

	result = ""
	while num > 0:
		result += random.choice(string.digits)
		num -=1
	
	return result

# Adding the chars to the password
def password_chars(password, pass_len, sample_set):
	
	tempt = password
	while len(tempt) < pass_len:
		tempt += random.choice(sample_set)
		
	if tempt == tempt.swapcase():
		password_chars(password, pass_len, sample_set)

	password = tempt
	return password
	

# Then I need to put it all together.

# Re-read code (I am SUPER tired right now).
# run 

def main():
	
	# Satisfoes password length requirement
	pass_len = password_length()

	# Choose sample set
	sample_set = useable_chars()
	
	# Satisfies the 1 digit requirement
	password = random.choice(string.digits)

	password = password_chars(password, pass_len, sample_set)
	# Satifies the at least one upper and lower case letter
	
	# Randomizes the password chars order
	password = "".join(random.sample(password,pass_len))
		
	print password

if __name__ == "__main__":
	main()

	
