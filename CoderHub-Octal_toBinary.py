#قم بكتابة function تستقبل متغير من نوع int يعبر عن قيمة ثمانية octal number،
# ثم قم بإرجاع النتيجة بعد التحويل الى قيمة ست عشرية binary number بنوع string
def oct_to_dec(octal):
	str1 = str(octal)
	j = 0
	num_dec = 0
	for i in range(len(str1)-1,-1,-1):
		base = pow(8,j)
		j+=1
		num_dec += int(str1[i])*base
	num_bin_string = str(bin(num_dec))
	num_dec_string = num_bin_string[2:len(num_bin_string)]
	return num_dec_string






print(oct_to_dec(1000))