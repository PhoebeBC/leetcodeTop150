check_list = [4,6,4,3,2,3,2,0,1,2] # 4,3,2,1


def check_max_val_ahead(jump: list, element: int, index: int) -> list:
    max_val = jump[index]
    max_val_index = index
    max_sight = max_val + max_val_index

    for idx in range(index, index + element):
        val = jump[idx]
        sight = val + idx
        if sight >= max_sight:
            max_sight = sight
            max_val = val
            max_val_index = idx

    return [max_val, max_val_index]


def minimum_jumps(jump):
    jumps = 1
    index = 0
    value = jump[index]

    while len(jump) - 1 > value + index:
        value, index = check_max_val_ahead(jump, value, index + 1)
        jumps += 1
    return jumps


print(minimum_jumps(check_list))
