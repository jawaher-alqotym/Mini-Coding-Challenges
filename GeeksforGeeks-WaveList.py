
# Function to sort the array into a wave-like array.
# input -> [1,2,3,4,5]   output -> 2 1 4 3 5
def convertToWave(arr):
    arr.sort()
    for i in range(0, len(arr), 2):
        if( i != len(arr)-1):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

        else:
            return arr
    return arr

s = [2,4,7,8,9,10]
print(convertToWave(s))
