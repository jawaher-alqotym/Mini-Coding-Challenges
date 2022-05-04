#قم بكتابة function تستقبل قيمة نصية string تعبر عن الساعة كنظام 12 أو 24 ساعة
# وتقوم بالتحويل بينها وقم بإلحاق نظام 12 ساعة بـ am أو pm
# ، ثم قم بارجاع النتيجة من نوع string

def convert_time(time):
  am = time.find('am')
  pm = time.find('pm')
  if am == -1 and pm == -1:
    return convert_toAmorPm(time)
  else:
    return convert_to24(time,am)

def convert_toAmorPm(time):

  n = int(time[0:2:].replace(":",''))
  if n <= 12:
    return time+"am"
  else:
    n = n - 12
    return str(n)+time[2:5]+'pm'

def convert_to24(time,am,pm):
  n = 0

  if am != -1 and time[0:2:] != '12':
    return (time[0:5:])
  elif am == -1:
    temp_str = time[0:2:].replace(' ','').replace(':','')
    if temp_str != '12':
     n = int(temp_str)+12
    else:
      n = int(temp_str)
    temp_str2 = time[2:5:].replace(':','').replace('p','')
    return (str(n)+":"+temp_str2)
  else:# it is 12:00 am
    return ('00:00')




print(convert_time('5:05'))

