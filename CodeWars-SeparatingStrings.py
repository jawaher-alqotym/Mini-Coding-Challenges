
# Create a function that takes a string and separates it into a sequence of letters.
# Input:"Just Live Life Man"
# The function should separate each word into individual letters,
# with the first word in the sentence having its letters in the 0th index 
# of each 2nd dimension array, and so on.
# The array will be formatted as so:
# [['J','L','L','M']
# ,['u','i','i','a']
# ,['s','v','f','n']
# ,['t','e','e','']]

def sep_str(st):
    bf_list = [(' '.join(i)).rsplit(' ') for i in st.split()]
    af_list =[]
    try:
     af_list_range = max([len(i) for i in bf_list])
    except ValueError:
        af_list_range = 0

    for i in range(af_list_range):
        temp = []
        temp.clear()
        for n in range(len(bf_list)):
            try:
             temp.append(bf_list[n][i])
            except IndexError:
             temp.append('')

        af_list.append(temp)

    return af_list


print(sep_str('The Mitochondria is the powerhouse of the cell'))
