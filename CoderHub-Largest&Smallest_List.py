#Write a function that receives an array of type integer
# and returns the largest and smallest number in the array.
def largest_smallest(array):
  array.sort()
  return [array[len(array)-1], array[0]]


ar = [32 , 44 , 9 , 3 , 8]
print(largest_smallest(ar))
