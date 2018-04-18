import re

spaceRegex = re.compile(r'(^\s+)|(\s+$)')

def strip(*arg):
	if len(arg) == 1:
		newStr = spaceRegex.sub('', arg[0])
	else:
		charRegex = re.compile(r''+arg[1])
		newStr = charRegex.sub('', arg[0])
	return newStr	
print(strip('   dicks in a cockbasket '))
print(strip('dunts in a cuntfluster '))
print(strip('fuckbags in a fuckshop fuck fuck cunt fuck', 'fuck'))
