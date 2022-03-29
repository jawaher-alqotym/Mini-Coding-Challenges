
#Given an array Arr of N positive integers.
# Your task is to find the elements whose value is equal to that of its index value
# ( Consider 1-based indexing ).

def valueEqualToIndex( arr, n):
   arr2= ''
   if(arr[0] == 1 ):
       arr2 += str(arr[0])
       arr2 += ' '

   for i in range(1, n, 1):
       if(i+1 == arr[i]):
           arr2 += str(arr[i])
           arr2 += ' '


   return arr2

Arr = [15, 2, 45, 12, 7, 6, 77, 8]
print(valueEqualToIndex(Arr, len(Arr)))