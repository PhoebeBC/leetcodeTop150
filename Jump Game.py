check_list = [3, 2, 1, 1, 0]


def find_zeros(jump_list):
    index_of_zeros = []

    for i in range(0, len(jump_list)-1):
        if jump_list[i] == 0:
            index_of_zeros.append(i)

    return index_of_zeros


def can_skip_zero(jump_list, zero_index):
    result = False

    for element_index in range(0, zero_index):
        if jump_list[element_index] >= 1 + zero_index - element_index:
            result = True

    return result


def is_jump_list(jump):
    if min(jump) > 0:
        return True

    result = True
    for zero_index in find_zeros(jump):
        if can_skip_zero(jump, zero_index) is False:
            result = False
    return result


print(is_jump_list(check_list))

# current_max_val = 0
# for val in jump:
#     if val > current_max_val:
#         current_max_val = val
#     if current_max_val == 0:
#         return False
#     current_max_val -= 1
# return True