def sum_list_abs(arr_):
    abs_arr = []
    for i in range(len(arr_)):
        abs_arr.append(abs(arr_[i]))

    return sum(abs_arr)

