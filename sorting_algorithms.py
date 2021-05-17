# IMPLEMENTATION OF ALL SORTING ALGORITHMS


# Selection Sort
def find_smallest_item(search_arr):
    """
    Finds and returns the smallest integer
    in array

    :param search_arr: array of integers
    :return: smallest item in search array
    """

    smallest_integer = search_arr[0]

    index = 1
    while index < len(search_arr):
        if search_arr[index] < smallest_integer:
            smallest_integer = search_arr[index]
        else:
            pass

        index += 1

    return smallest_integer


def selection_sort(arr):
    """
    Sorts input array in ascending order

    :param arr: array to be sorted
    :return: sorted array
    """

    sorted_arr = list()  # Array to contain sorted items

    while len(arr) > 0:
        search_item = find_smallest_item(search_arr=arr)
        arr.remove(search_item)
        sorted_arr.append(search_item)

    return sorted_arr


input_arr = [7, 1, 4, 10, 3, 9, 11]  # Test array
print(selection_sort(arr=input_arr))
