#Write a function that receives a value of type string
# The function extracts the character in the middle
# of the word and then returns the character of type string

def middle_char(word):
 str1 = ''
 s = len(word)
 if s % 2 == 0:
  b = int(s/2)+1
  a = int(s/2-1)
  str1 = word[a:b:1]
 else:
  c = int((s/2))
  str1 = word[c]

 return str1

print(middle_char('cook'))
