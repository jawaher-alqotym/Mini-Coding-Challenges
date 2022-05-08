
# Create a function that takes a string and separates it into a sequence of letters.
# The function should separate each word into individual letters,
# with the first word in the sentence having its letters in the 0th index 
# of each 2nd dimension array, and so on.
#----
# Input:"The Mitochondria is the powerhouse of the cell"
# The array will be formatted as so:
# => [ [ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
# => [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
# => [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
# => [ '', 'o', '', '', 'e', '', '', 'l' ],
# => [ '', 'c', '', '', 'r', '', '', '' ],
# => [ '', 'h', '', '', 'h', '', '', '' ],
# => [ '', 'o', '', '', 'o', '', '', '' ],
# => [ '', 'n', '', '', 'u', '', '', '' ],
# => [ '', 'd', '', '', 's', '', '', '' ],
# => [ '', 'r', '', '', 'e', '', '', '' ],
# => [ '', 'i', '', '', '', '', '', '' ],
# => [ '', 'a', '', '', '', '', '', '' ]]

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
