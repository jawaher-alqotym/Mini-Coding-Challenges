
#قم بكتابة function تستقبل قيمة نصية من نوع string تقوم الـ function بترتيب الكلمات حسب طولها
# من الأقصر للأطول وفي حال كانت هناك كلمتين بنفس الطول يكون الترتيب ابجدي
# ثم قم بارجاع النتيجة من نوع string

def sortByLength(txt):
    elem_len = {i:len(i) for i in txt.split()}#'word a'->{word:4, a:1}
    sorted_by_val = sorted(elem_len.items(), key=lambda kv:kv[1])#lambda [parameter]:expresion
    #{word:4, a:1}->[('a',1),('word',4)]
    list1 = [i[0] for i in sorted_by_val ]#[('a',1),('word',4)]->['a','word']
    str1 = ' '.join(list1)#['a','word']->"a word"
    return str1

print(sortByLength('Have a nice day'))


