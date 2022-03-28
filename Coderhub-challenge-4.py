#Write a function that receives an array of type integer,
#

#Approach #1 : Naive Approach
def most_frequent_element(arr):
 freq = 0
 temp = 0
 val = None
 for i, j in enumerate(arr):
  temp = freq
  freq = arr.count(j)

  if(freq <= temp ):
       freq = temp
       val = arr[i-1]

 return val, freq


ar = [1 , 2 , 3 , 4 , 1 , 5 , -5 , -5 , -5 , -5 , -5 , 6]
print(most_frequent_element(ar))

