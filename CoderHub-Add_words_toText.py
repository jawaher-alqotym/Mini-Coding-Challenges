#Write a function that receives two values,
# one of type integer and one of type string,
# then the function adds the word Hi or Bye to the name entered so that
# Hi =1, Bye= 0 and then returns the result of type string.

def say_hi_bye(name, num):
    str1 = ''
    list1 = []
    list1.append(name)
    list1.append(' ')
    if (num == 0):
        list1.append('Bye')

    elif (num == 1):
        list1.append('Hi')

    for i in range(len(list1)):
        str1 += list1.pop()

    return str1

print(say_hi_bye('Ahmad',1))