
#Given a string s, extract all the integers from s.
#Example 1 Input: "1: Prakhar Agrawal, 2: Manish Kumar Rai,  3: Rishabh Gupta56"
#Output: 1 2 3 56

def extractIntegerWords(s):
    s += ' '
    s2 = ''
    for i ,j in enumerate(s):
        if (j.isdigit() == True):
            s2 += j
            if(s[i+1].isdigit() == False):
                 s2 += ' '
            else:
                continue


    return s2


Teast = "1: Prakhar Agrawal, 2: Manish Kumar Rai,  3: Rishabh Gupta56"
print(extractIntegerWords(Teast))
