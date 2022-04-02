
#You are given a string s. You need to reverse the string.

def reverseWord(s):#Geeks
    str2 = " ".join(s)#G e e k s
    list1 = str2.rsplit(" ")#['G', 'e', 'e', 'k', 's']
    list1.reverse()#['S', 'e', 'e', 'G']
    str3 = ''.join(list1)

    return str3


print(reverseWord('Geeks'))
