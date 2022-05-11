
# A Narcissistic Number is a positive number which is the sum of its own digits
# each raised to the power of the number of digits in a given base. In this Kata
# we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcisstic:
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:
#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# The Challenge: Your code must return true or false (not 'true' and 'false')
# depending upon whether the given number is a Narcissistic number.


def M1_narcissistic( value ):# Using map
    str_value = str(value)
    n = len(str_value)
    return value == sum(map(lambda c: pow(c, n), map(int, str_value)))


def M2_narcissistic( value ):# Alternative solution using list comprehension.
    value_str = str(value)
    n = len(value_str)
    return value ==  sum([pow(int(i),n) for i in value_str])

print(M1_narcissistic(153))
print(M2_narcissistic(153))
print(M1_narcissistic(1652))
print(M2_narcissistic(1652))
