"""
Creatting a password generator for fun.

Requirements:
	1. At least one digit
	2. At lease one uppercase letter
	3. At least one lowercase letter
	4. A string of length x, where 6<=x<=12
"""

import random, string

def main():
	
	# Satisfoes password length requirement
	pass_len = random.randint(6,12)
	
	# Satisfies the 1 digit requirement
	password = random.choice(string.digits)

	while len(password) <=pass_len:
		password += random.choice(string.printable[:62])
	
	# Satifies the at least one upper and lower case letter
	if password.swapcase() == password:
		main()
	else:
		password = "".join(random.sample(password,pass_len))
		
	print password

if __name__ == "__main__":
	main()

	
