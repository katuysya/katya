from math import sqrt
arr = input().split()
def get_all_permutatons(nums_array):
    if len(nums_array) == 1:
        return[nums_array]
    res = []
    for i in range(len(nums_array)):
        curr_num = nums_array[i]
        remaining = nums_array[:i] + nums_array[i+1:]
        for elems in get_all_permutatons(remaining):
            res.append(([curr_num] + elems))

    return res
print(get_all_permutatons(arr))
