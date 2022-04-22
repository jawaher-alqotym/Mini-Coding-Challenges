#Write a function that receives a value of type string
# The function switches the case of the letters,
# converting the lowercase to the uppercase and vice versa,
# and then returns the value of the type string

def reverse_case(str):
  str2=''
  for i in range(len(str)):
    if(str[i].isupper()):
      str2= str2+str[i].lower()
    elif(str[i].islower()):
        str2 = str2 + str[i].upper()


  return str2


print(reverse_case('WeLcomE'))