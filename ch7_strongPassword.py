import re

passwdRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)([a-zA-Z\d!@#$%^&*()<>?]{8,})')

def testPasswdStrength(passwd):
	lowerRegex = re.compile(r'[a-z]')
	upperRegex = re.compile(r'[A-Z]')
	digitRegex = re.compile(r'[0-9]')
	if len(passwd) < 8:
		print('Your password is too short, it should be at least 8 characters.')
	elif lowerRegex.search(passwd) is None:
		print('Your password must contain at least 1 lowercase letter.')
	elif upperRegex.search(passwd) is None:
		print('Your password must contain at least 1 uppercase letter.')
	elif digitRegex.search(passwd) is None:
		print('Your password must contain at least 1 number.\n')
	else:
		print('Your password is strong.')

print('Type your password:')
passwd = input()
testPasswdStrength(passwd)
