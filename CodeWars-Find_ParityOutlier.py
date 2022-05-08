
# You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. The array is either entirely comprised of odd integers
# or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    list_odd = [i for i in integers if i % 2 != 0]
    list_even = [i for i in integers if i % 2 == 0]
    return list_odd[0] if len(list_odd) < len(list_even) else list_even[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))# -> 11 (the only odd number)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))# -> 160 (the only even number)

