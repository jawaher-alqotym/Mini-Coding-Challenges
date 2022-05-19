'''
Complete the function scramble(str1, str2)
that returns true if a portion of str1 characters can be rearranged to match str2,
otherwise returns false.
Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
'''

def scramble(s1, s2):
    set1, set2 = set(s1), set(s2)
    print(set1&set2)
    return True if set1 & set2 == set2 else False


print(scramble('scriptjava', 'javascript'))
print(scramble('katas', 'steak'))
print(scramble('scriptingjava', 'javascript'))