#Write a function that receives two arrays of type integer,
# and the function subtracts the items in the first array from the items in the second array,
# and then returns an array of type integer that is the sum of the subtracted arrays
def sub_arrays(arr1, arr2):
 arr3 = []
 for i in range(len(arr1)):
     arr3.append(arr2[i]-arr1[i])

 return arr3

arrr1 = [93 , 22 , 7]
arrr2 = [-3 , 4 , 0]
print(sub_arrays(arrr1, arrr2))
