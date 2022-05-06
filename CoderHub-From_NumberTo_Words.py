#0-999
def numToEng(n):
    num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
                 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
                 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
                 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
                 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
                 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
                 90: 'ninety', 0: 'zero', 100: 'one hundred',\
                 200: 'tow hundred', 300: 'three hundred', 400: 'four hundred',\
                 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred',\
                 800: 'eight hundred', 900: 'nine hundred'}
    n_str = str(n)
    try:
      return num2words[n]
    except KeyError:
      try:

        if n < 100:
          first = n_str[0]+'0'
          second = n_str[1]
          return num2words[int(first)] +'-'+ num2words[int(second)]

        elif n < 1000:
          first = n_str[0]
          second = 'hundred'
          third = n_str[1:3]
          return num2words[int(first)]+' '+second+' '+num2words[int(third)]

      except KeyError:
        try:
          if n < 1000:
            first = n_str[0]
            second = 'hundred'
            third = n_str[1:2]+ '0'
            fourth = n_str[2]
            return num2words[int(first)] + ' ' + second + ' and ' + num2words[int(third)] + ' ' + num2words[int(fourth)]
        except KeyError:
          return 'out of range'
    return 'out of range'




print(numToEng(999))