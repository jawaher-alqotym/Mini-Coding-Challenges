
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