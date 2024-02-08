def sum_binary_strings(a, b):
    a_len = len(a)
    b_len = len(b)
    len_max = max(a_len, b_len) + 1
    binary_sum_list = [0] * len_max
    a_diff = len_max - a_len
    b_diff = len_max - b_len
    a_adj = str("0" * a_diff) + a
    b_adj = str("0" * b_diff) + b

    a_list = list(a_adj)
    for idx in range(len(a_adj)):
        a_list[idx] = int(a_list[idx])

    b_list = list(b_adj)
    for idx in range(len(b_adj)):
        b_list[idx] = int(b_list[idx])

    carry = 0
    for idx in range(1, len_max + 1):
        sum_ab = a_list[len_max - idx] + b_list[len_max - idx] + carry
        if sum_ab == 3:
            binary_sum_list[len_max - idx] = 1
            carry = 1
        elif sum_ab == 2:
            carry = 1
        elif sum_ab == 1:
            binary_sum_list[len_max - idx] = 1
            carry = 0
        else:
            carry = 0

    if binary_sum_list[0] == 0:
        binary_sum_list.pop(0)

    binary_sum_str = ""
    for element in binary_sum_list:
        binary_sum_str += str(element)

    return binary_sum_str


print(sum_binary_strings("01010001",
                         "1110011101010101"))

