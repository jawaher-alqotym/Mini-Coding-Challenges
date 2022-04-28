# Given an unsorted array A of size N
# that contains only non-negative integers,
# find a continuous sub-array which adds to a given number S.
# In case of multiple subarrays, return the subarray which comes first
# on moving from left to right.
def subArraySum(arr, n, s):
    j = 0
    sum = 0
    list1 = []

    while j < n:
        for i in range(j, n):
            list1.append(i)
            sum += arr[i]
            if sum == s:
                break

        if sum != s:
            list1.clear()
            sum = 0
            j += 1
        else:
            break

    x = len(list1)

    if x == 0:
        return [-1]
    else:
        return 'Values in indexes ',[list1[0] + 1, list1[x - 1] + 1],'results in',s
    
list = [107, 41, 143, 65, 49]
s = 184
print(subArraySum(list,len(list),s))

