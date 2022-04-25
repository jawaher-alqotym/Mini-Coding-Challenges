#Write a function that receives a value of type string
# The function removes all symbols like ($,!, @, #,.)
# except the ( '-', '_' ) and returns the string after the removal

def removeSpecialCharacters(str):
	str2 = ''
	for j in str:
	  if j.isalpha() or j == '-' or j == '_' or j == ' ':
	    str2 += j
	return str2

print(removeSpecialCharacters('her 88name i@s -Sara-??'))