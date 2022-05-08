
# the start number and the end number of a region and should return the count
# of all numbers except numbers with a 5 in it.
# The start and the end number are both inclusive!
# 1,9 -> [1,2,3,4,6,7,8,9] , count 8 numbers
# 4,17 -> [4,6,7,8,9,10,11,12,13,14,16,17] , count 12 numbers

def dont_give_me_five(start,end):
    list = ([i for i in range(start,end+1) if i % 10 != 5 \
             and i-i % 10 != 50 \
             and i-i % 10 - 100 != 50])
    return list, len(list)


print(dont_give_me_five(1, 9))
print(dont_give_me_five(34, 66))
