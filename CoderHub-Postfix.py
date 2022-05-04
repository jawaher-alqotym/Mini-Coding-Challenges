
#قم بكتابة function تستقبل قيمة نصية من نوع string ، تقوم الـ function باستقبال معادلة رياضية
#ولكن العمليات الرياضية تكون لاحقة postfix ، ثم تقوم الـ function بحلها وإرجاع النتيجة من نوع integer

def postFix(expr):
    stack = []
    expr = expr.rsplit(" ")
    for i in expr:
        if i.isdigit():
            stack.append(int(i))

        elif i == '+':
            stack.append(stack.pop() + stack.pop())

        elif i == '-':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b-a)

        elif i == '*':
            stack.append(stack.pop() * stack.pop())

        elif i == '/':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b/a)

    return int(stack.pop())


print(postFix('10 2 8 * + 3 -'))