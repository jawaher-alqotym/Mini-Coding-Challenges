
#You are given a string s. You need to reverse the string.

def reverseWord(s):#Geeks
    str3 = ''
    str2 = " ".join(s)#G e e k s
    list1 = str2.rsplit(" ")#['G', 'e', 'e', 'k', 's']
    list1.reverse()#['S', 'e', 'e', 'G']
    for i in list1:#reverse the list back to string
        str3 += i

    return str3


print(reverseWord('Geeks'))
