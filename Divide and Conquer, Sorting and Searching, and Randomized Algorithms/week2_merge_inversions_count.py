def split(input_list):
    """
    Splits a list into two pieces
    :param input_list: list
    :return: left and right lists (list, list)
    """
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]


def merge_sorted_lists_inv_count(list_left, list_right, prev_inv_count):
    """
    Merge two sorted lists
    This is a linear operation
    O(len(list_right) + len(list_right))
    :param list_left: list
    :param list_right: list
    :param prev_inv_count: int
    :return merged list
    """
    # Special case: one or both of lists are empty
    if len(list_left) == 0:
        return list_right, 0
    elif len(list_right) == 0:
        return list_left, 0

    # General case
    index_left = index_right = 0
    list_merged = []  # list to build and return
    list_len_target = len(list_left) + len(list_right)
    inv_count = 0
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            # Value on the left list is smaller (or equal so it should be selected)
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            # Right value bigger
            list_merged.append(list_right[index_right])
            index_right += 1
            inv_count += len(list_left) - index_left

        # If we are at the end of one of the lists we can take a shortcut
        if index_right == len(list_right):
            # Reached the end of right
            # Append the remainder of left and break
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            # Reached the end of left
            # Append the remainder of right and break
            list_merged += list_right[index_right:]
            break

    return list_merged, inv_count + prev_inv_count


def merge_sort_inv_count(input_list, inv_count=0):
    """
    Sort two lists and count inversions
    This is a n*log(n), n=len(input_list)
    :param input_list: list
    :param inv_count: int
    :return merged list, amount of inversions
    """
    if len(input_list) <= 1:
        return input_list, inv_count
    else:
        left, right = split(input_list)
        # The following line is the most important piece in this whole thing
        result_left, result_right = merge_sort_inv_count(left), merge_sort_inv_count(right)
        inv_count += result_left[1] + result_right[1]
        return merge_sorted_lists_inv_count(result_left[0], result_right[0], inv_count)


print(merge_sort_inv_count([9, 1]))
print(merge_sort_inv_count([9, 1, 10, 2]))
print(merge_sort_inv_count([9, 8, 1, 10, 3, 2]))

with open('week2_IntegerArray.txt', 'r') as list_of_int:
    unsorted_array = [int(x) for x in list_of_int]
    print(merge_sort_inv_count(unsorted_array)[1])
