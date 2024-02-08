# Group of children, each must have at leat on peice of candy
# Peices of candy are decided by neightbours rankings
'''
# Solution:
# start with all children that are ranked 0 and give 1 sweet,
# then repeat with rankings 1, each time check neighbour, if neighbour is smaller then
# add one sweet to the number of sweets the max neighbour has,
# repeat until you have all children covered


[1,2,1,2,1,2,1,1,1,1]
'''

break_dans = [0, 1, 3, 5, 4, 3, 2, 1, 0]  # 2,1,2,1,1,2 = 9
check = [1, 2, 3, 6, 5, 4, 3, 2, 1]


# ranking_list = [1, 2, 2]
#    [2, 1, 2, 3, 4, 1, 2, 1, 2] = 18


def dedupe_ascend(dog_ranking):
    ranking_ordered = []
    for rank in dog_ranking:
        if rank not in ranking_ordered:
            ranking_ordered.append(rank)
    ranking_ordered.sort()
    return ranking_ordered


def find_indices_of_rank(dog_ranking, rank):
    indices_of_rank = []
    for idx in range(0, len(dog_ranking)):
        if dog_ranking[idx] == rank:
            indices_of_rank.append(idx)
    return indices_of_rank


def give_rank_treats(dog_ranking, number_of_treats, rank):
    # getting positions of all the dogs with the current rank
    indices_of_rank = find_indices_of_rank(dog_ranking, rank)

    # going through each index to check this rank's neighbours
    for idx in indices_of_rank:
        # Doing cases for if the rank is the first or last as then
        # we only need to check one neighbour
        # As we are going through the ranks in ascending order,
        # any ranks smaller than the current rank will already have
        # their number of treats assigned
        if idx == 0:  # Start of dog ranking list
            if dog_ranking[idx] > dog_ranking[idx + 1]:
                number_of_treats[idx] = number_of_treats[idx + 1] + 1
            else:
                number_of_treats[idx] = 1
        elif idx == len(dog_ranking) - 1:  # End of dog ranking list
            if dog_ranking[idx] > dog_ranking[idx - 1]:
                number_of_treats[idx] = number_of_treats[idx - 1] + 1
            else:
                number_of_treats[idx] = 1
        else:
            if dog_ranking[idx] > dog_ranking[idx + 1] or dog_ranking[idx] > dog_ranking[idx - 1]:
                number_of_treats[idx] = max(number_of_treats[idx + 1], number_of_treats[idx - 1]) + 1
            else:
                number_of_treats[idx] = 1

    return number_of_treats


def min_treats(dog_ranking):
    # Making a list to contain the number of dog treats for each dog
    number_of_treats = [0] * len(dog_ranking)  # WORKING
    # creating a list of the dog rankings in ascending order
    # without duplicates, so we can work our way through the rankings from
    # bottom to top to assign treats
    ranking_ordered = dedupe_ascend(dog_ranking)  # WORKING

    # going through each dog ranking to assign treats to the ranking SOME REASON GIVING MORE VALUES THAN NECESARY
    for rank in ranking_ordered:
        # If the ranking is the smallest we assign the number of treats to be 1
        # as each dog needs at least one sweet
        if rank == min(ranking_ordered):  # WORKING
            min_rank = find_indices_of_rank(dog_ranking, rank)
            for idx in min_rank:
                number_of_treats[idx] = 1
        # Otherwise we need to check if the current rank has a smaller rank either side
        # If it does, we need to give that dog an extra sweet
        else:
            # Getting the number of treats for each dog with the rank
            give_rank_treats(dog_ranking, number_of_treats, rank)

    return sum(number_of_treats)


print(min_treats(break_dans))
print(sum(check))
