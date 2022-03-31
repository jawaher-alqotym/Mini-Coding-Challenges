# Write a function that takes two positive integers
# the function subtracts the two numbers without using the - sign
# and then returns the result of the subtraction operation
def subtract(num1, num2):
    c = 0
    s = num1
    b = num2
    if (num1 > num2):
        s = num2
        b = num1

    for i in range(s, b):
            c += 1

    if(num1 < num2):
        c = c * -1
    return c





print(subtract(33, 60))