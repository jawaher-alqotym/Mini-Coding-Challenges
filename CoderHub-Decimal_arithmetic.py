#Write a function that receives a value of type string
# the input contains a decimal or integer then the function counts
# the number of digits after the point and returns the result of type integer

def Decimal_Number(num):
 count =0
 str1 = str(num)
 lenth = len(str1)
 s =str1.find('.',0,lenth)

 if (s != -1):
  for i in range(s,lenth-1,1):
     count+=1
  return count
 else:
     return 0


print(Decimal_Number(8.99))

