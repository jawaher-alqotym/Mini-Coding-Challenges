
#قم بكتابة function تستقبل متغير من نوع string يعبر عن قيمة ثمانية binary number،
# ثم قم بإرجاع النتيجة بعد التحويل الى قيمة ست عشرية octal number بنوع int
def bin_to_oct(b):
   num_bin = int(b,2)
   num_oct = oct(num_bin)
   str1 = str(num_oct)#to remove the 0o from 234: 0o234 -> 234
   list1 = [i for i in str1]
   list1.pop(0)
   list1.pop(0)
   str2 = ''.join(list1)

   return int(str2)


print(bin_to_oct('10011100'))#10011100->234

