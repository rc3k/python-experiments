import math


def count_numbers(sorted_list, less_than):
    if less_than > sorted_list[-1]:
        return len(sorted_list)

    if sorted_list[0] >= less_than:
        return 0

    midway = math.floor(len(sorted_list) / 2)

    if sorted_list[midway - 1] < less_than and sorted_list[midway] >= less_than:
        return midway

    if sorted_list[midway] < less_than:
        return count_numbers(sorted_list[midway:], less_than) + midway

    else:
        return count_numbers(sorted_list[0: midway], less_than)


if __name__ == "__main__":
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 9, 1000]
    print(count_numbers(sorted_list, 3))  # should print 2
