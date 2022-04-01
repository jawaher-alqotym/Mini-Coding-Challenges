
# قم بكتابة function تستقبل عدد صحيح من نوع integer
# ، تقوم الـ function بجمع الأعداد الفردية والزوجية التي يتكون منها الـ integer المدخل
# وإرجاع النتيجة من نوع string، في حال كان مجموع الأعداد الفردية أكبر من مجموع الأعداد الزوجية قم بارجاع odd ،
# وفي حال كان مجموع الأعداد الزوجية أكبر من مجموع الأعداد الفردية قم بإرجاع even
# و في حال كان مجموع الأعداد الفردية يساوي مجموع الأعداد الزوجية قم بإرجاع equal
# Example1: num = 561 -> output:equal, explanation: odd=5+1 , even=6
# Example2: num = 132 -> output:odd, explanation: odd=1+3 , even=2

def oddsVsEvens(num):
    even = []
    odd = []
    s = str(num)
    s = " ".join(s)#5 6 1
    list1 = s.rsplit(" ")#['5', '6', '1']
    for i in list1:
      if(int(i) % 2 == 0):
        even.append(int(i))
      else:
         odd.append(int(i))

    sumOdd = sum(odd)
    sumEven = sum(even)
    if(sumOdd == sumEven):
        return 'equal'
    elif( sumOdd > sumEven):
        return 'odd'
    else:
        return 'even'


print(oddsVsEvens(561))