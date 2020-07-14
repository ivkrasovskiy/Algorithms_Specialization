from random import randrange


def choose_pivot(array: list, n: int, pivot_option=None, l=None, r=None) -> int:
    """
    :param array: a given array
    :param n: array length
    :param pivot_option: how to choose element for pivoting
    :return: pivot element and its index based on the pivot option. If not given, then random
    """
    if pivot_option == 'first':
        return l
    elif pivot_option == 'last':
        return r - 1
    elif pivot_option == 'median_of_three':  # median among first, last and median
        if n % 2 == 1:
            three_elem = [(array[l], l), (array[l + n // 2], l + n // 2), (array[r - 1], r - 1)]
        else:
            three_elem = [(array[l], l), (array[l + n // 2 - 1], l + n // 2 - 1), (array[r - 1], r - 1)]
        three_elem.sort(key=lambda tup: tup[0])
        return three_elem[1][1]

    return randrange(l, r, 1)


def partition(array: list, l: int, r: int) -> int:
    """
    :param array: unpartitioned array
    :param l: an element that is one position to the left from a pivot element
    :param r: an element that is one position to the right from a pivot element
    :return:
    """
    p = array[l]
    i = l + 1

    for j in range(l + 1, r, 1):
        if array[j] < p:
            array[j], array[i] = array[i], array[j]
            i += 1

    array[l], array[i - 1] = array[i - 1], array[l]
    return i - 1


def quicksort(array: list, pivot_option=None, l=None, r=None) -> list:
    """
    Sorts array defining how to choose a pivot element
    :param array: unsorted array
    :param pivot_option: how to choose the pivot element
    :param l: if elements before number l in array are presorted
    :param r: if elements before number r in array are presorted
    :return: sorted array
    """

    if r is None:
        array_len = len(array)
        l = 0
        r = len(array)
    else:
        array_len = r - l + 1

    if array_len <= 1:
        return array

    p = choose_pivot(array, array_len, pivot_option, l, r)
    array[l], array[p] = array[p], array[l]

    new_p = partition(array, l, r)

    l1 = l
    r1 = new_p - 1
    quicksort(array, pivot_option, l1, r1 + 1)

    l2 = new_p + 1
    r2 = r
    quicksort(array, pivot_option, l2, r2)

    return array


def partition_swaps_counter(array: list, l: int, r: int) -> tuple:
    """
    :param array: unpartitioned array
    :param l: an element that is one position to the left from a pivot element
    :param r: an element that is one position to the right from a pivot element
    :return:
    """
    p = array[l]
    i = l + 1

    swaps = 1
    for j in range(l + 1, r, 1):
        if array[j] < p:
            array[j], array[i] = array[i], array[j]
            i += 1
            swaps += 1

    array[l], array[i - 1] = array[i - 1], array[l]  # +1 to swaps
    return (i - 1, swaps + 1)


def quicksort_swaps_counter(array: list, pivot_option=None, l=None, r=None) -> int:
    """
    Sorts array defining how to choose a pivot element
    :param array: unsorted array
    :param pivot_option: how to choose the pivot element
    :param l: if elements before number l in array are presorted
    :param r: if elements before number r in array are presorted
    :return: sorted array
    """

    if r is None:
        array_len = len(array)
        l = 0
        r = len(array)
    else:
        array_len = r - l + 1

    if array_len <= 1:
        return 0

    p = choose_pivot(array, array_len, pivot_option, l, r)
    array[l], array[p] = array[p], array[l]  # first swap

    new_p, current_swaps = partition_swaps_counter(array, l, r)
    #but for coursera just current_use: swaps = r - l

    l1 = l
    r1 = new_p - 1
    swaps_left = quicksort_swaps_counter(array, pivot_option, l1, r1 + 1)

    l2 = new_p + 1
    r2 = r
    swaps_left_right = quicksort_swaps_counter(array, pivot_option, l2, r2)

    return swaps_left + swaps_left_right + current_swaps


print(quicksort([6, 5, 7, 3, 4, 8, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8])
print(quicksort_swaps_counter([6, 5, 7, 3, 4, 8, 2, 1], pivot_option='first'))

with open('week3_QuickSort.txt', 'r') as list_of_int:
    unsorted_array = [int(x) for x in list_of_int if x is not None]
    print(quicksort_swaps_counter(unsorted_array, pivot_option='first'))

#162085, 164123, 138382
