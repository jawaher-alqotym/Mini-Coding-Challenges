
# two words are anagrams of each other if they both contain the same letters.
# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none.

def anagrams(word, words):
 temp = sorted(word)
 return [item for item in words if sorted(item) == temp]

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) # -> ['aabb', 'bbaa']
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))# -> ['carer', 'racer']





