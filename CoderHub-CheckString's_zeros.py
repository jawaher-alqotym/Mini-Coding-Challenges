#قم بكتابة function تستقبل قيمة نصية من نوع string
# عبارة عن سلسلة مكونة من الرقم (1 و 0) ،
# تقوم الـ function بإرجاع أطول سلسلة من الأصفار المتتالية كقيمة نصية string.
# في حال عدم وجود أصفار في النص ، قم بإرجاع قيمة فارغة “ “.
def longestZero(str):
#will first count the num of 0 and if came acros 1
# will set the count back to 0 and start over countin
 count = 0
 list =[]
 for i in str:
     if i == '0':
      count+=1
      list.append(count)
     else:
       count=0
 if len(list)==0:
     return ''
 else:
     return '0'*max(list)


print(longestZero('10000100'))
