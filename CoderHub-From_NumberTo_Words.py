#0-999
import math

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero', 100:'hundred'}
def numToEng(n):
    try:
        print (num2words[n])
    except KeyError:
        try:
            print (num2words[n - n % 10].lower() +'-'+ num2words[n % 10].lower())
        except KeyError:
            try:
                hundreds = (n - n % 50)
                num_str = str(n)
                print(num2words[math.floor(n/100)].lower()+' '+num2words[hundreds-(hundreds-100)].lower()
                      +' '+num2words[int(num_str[1]+num_str[2])].lower())
            except KeyError:
                try:
                 num_str = str(n)
                 temp = int(num_str[1]+num_str[2])
                 print(num2words[math.floor(n/100)].lower()+' '+num2words[hundreds-(hundreds-100)].lower()
                      +' '+num2words[temp - temp % 10].lower() +' '+ num2words[temp % 10].lower())
                except:
                     print('Number out of range')


numToEng(808)
