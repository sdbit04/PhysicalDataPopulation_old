''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def main(input_nbr_p):
    # Write code here
    input_nbr = input_nbr_p
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    if 1 <= input_nbr <= 26:
        alpha_comb = None
        for index in range(1, input_nbr+1):
            if index == 1:
                alpha_comb = alphabet[0]
                print(' '*(input_nbr-1), end='')
                print(alpha_comb)
            else:
                alpha_comb = "{0} {1} {0}".format(alphabet[index-1], alpha_comb)
                print(" "*(input_nbr - index), end='')
                print(alpha_comb)

l1 = ['w', 'e']
def swap(list_1, ind_1, ind_2):
    list1 = list_1
    ind1 = ind_1
    ind2 = ind_2
    list1_ind1 = list1[ind1]
    list1[ind1] = list1[ind2]
    list1[ind2] = list1_ind1
    return list1


print(swap(l1, 0, 1))


def reverse(input_string):
    input_str = list(input_string)
    left_index = 0
    right_index = len(input_str) - 1
    while left_index < right_index:
        swap(input_str, left_index, right_index)
        left_index += 1
        right_index -= 1
    s = ''
    for i in input_str:
        s = "{}{}".format(s, i)
    return s


def reverse1(input_string: str):
    # as string is immutable, so we cust the object to list
    input_list = list(input_string)
    string_len = len(input_list)
    out_str = ""
    for i in range(string_len-1, -1, -1):
        out_str = "{}{}".format(out_str, input_list[i])
    return out_str


L1 = [1,3,5,8,14,18]
L2 = [2,6,13,20]


def merge_sorted_arrays(arr1: list, arr2: list):
    if arr1[-1] < arr2[-1]:
        list1 = arr2
        list2 = arr1
    else:
        list1 = arr1 # has bigger value at the end
        list2 = arr2
    list1_indx = 0
    max_list1_indx = len(list1)-1
    list2_indx = 0
    max_list2_indx = len(list2) - 1
    while list2_indx <= max_list2_indx:
        if list1[list1_indx] < list2[list2_indx]:
            list1_indx += 1
        else:
            list1.insert(list1_indx, list2[list2_indx])
            # as list2 last value is smaller, so it finnaly get an instruction to insert its last value to list1 and go
            # to next index, which doesnt exist, so we want to stop the while-loop, so while loop depends only
            #  list2 index
            list2_indx += 1
    return list1


def called_func(p):
    if p.isnumeric():
        print(" we have got a number")
    else:
        raise ValueError(" We are expecting a number")


def get_only_number(input_string): # number = '234,4,5j6;6;. -6734@ui'
    nbr = ""
    for char in input_string:
        if char.isnumeric():
            nbr = "{}{}".format(nbr, char)
    return int(nbr)


if __name__ == "__main__":
    # print(reverse1("swapan"))
    # print(reverse('Swapan'))
    # L1 = [1,3,5,8,14,18]
    # L2 = [2,6,13,20]
    # print(merge_sorted_arrays(L1, L2))
    # called_func('b')
    # value = "".join(str(i) if i >= 3 else "" for i in L1)
    # print(value)
    # number = '234,4,5j6;6;. -6734@ui'
    # nbr = get_only_number(number)
    # print(str(nbr))

    sector_carrier = 230925570
    result = sector_carrier/ 256
    int_part = sector_carrier // 256

    remainder = sector_carrier.__mod__(256)
    print(result)
    print(int_part)
    print(remainder)
