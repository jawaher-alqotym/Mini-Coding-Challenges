# Given an unsorted array A of size N
# that contains only non-negative integers,
# find a continuous sub-array which adds to a given number S.
# In case of multiple subarrays, return the subarray which comes first
# on moving from left to right.
def finde_indexes(arr,list1):
    list_indexses = [arr.index(i) for i in list1 ]
    return list_indexses

def subArraySum(arr, n, s):
    j = 0
    sum = 0
    list1=[]
    while j<n:
     for i in range(j,n):
        list1.append(arr[i])
        sum += arr[i]
        if sum == s:
            break

     if sum != s:
        list1.clear()
        sum=0
        j+=1
     else:
        break
    print('indexes:', finde_indexes(arr,list1),'which contain the values:',list1, " Sums to ", s)

list = [1,2,3,7,2]
s = 12
subArraySum(list,len(list),s)
