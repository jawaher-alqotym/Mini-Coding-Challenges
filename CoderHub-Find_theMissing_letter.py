#Write a function that receives a value of type string,
# the function searches for the missing character in alphabetical order
# for the first character entered in the text, then returns the missing character
# of type string and if no character is missing return a message stating that
def missingLetter(txt):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  alpha_index = alpha.index(txt[0])
  s = len(txt)+alpha_index
  alpha_sub = alpha[alpha_index:s:]
  j=0
  while j<len(alpha_sub):
    if(txt[j] != alpha_sub[j]):
     return alpha_sub[j]
    else:
     j+=1


  return 'No Missing Letter'

print(missingLetter('qrs'))