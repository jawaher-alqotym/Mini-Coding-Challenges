# Given an unsorted array A of size N
# that contains only non-negative integers,
# find a continuous sub-array which adds to a given number S.
# In case of multiple subarrays, return the subarray which comes first
# on moving from left to right.
def subArraySum(arr, n, s):
    res = []
    while arr:
        num = arr.pop()
        diff = s - num
        if diff in arr:
            res.append((diff, num))

    return res

list = [1,2,5,33,11,23,12,90,87,4]
s = 12
print(subArraySum(list,len(list),s))

