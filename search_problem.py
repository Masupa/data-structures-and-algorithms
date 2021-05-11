"""
    Search Algorithms are an important set of algorithms that can help us search for
    elements or items through a given set or containment of items.

    For example:
    1. Finding a word in a dictionary
    2. Finding the name of a person in a phone book
    3. Finding a number in a list of numbers between 1 and 100
    Etc
"""


"""
    Linear Search (Simple/Dumb :) Search)
    
    Linear search is an algorithm that searches through a set of items by visiting
    all items, one at a time. In the worst-case scenario, this algorithms takes O(n)
    time-complexity.
    
    This algorithms eliminates one potential element at a time, in solution
"""


def linear_search(list, item):
    """
    :param list: A list of integer numbers
    :param item: An integer number
    :return: Returns position of item in list is found, else None
    """

    for index, integer in enumerate(list):
        if integer == item:
            return index
    return None


# Sample List
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sample Search Item
item_ = 9

# return_result = linear_search(list=list_, item=item_)


"""
    Binary Search
    
    Binary Search is a search algorithms that searches for an item by 
    constantly dividing the search space into two halves depending on
    the condition. It runs at O(log n) time-complexity, where log is in
    base 2.
    
    Unlike linear search that eliminates one items at a time, Binary 
    Search eliminates half of the items as it progresses through.
    
    Compaired to linear search, this algorithms get's faster as the
    number of items grows
"""


def binary_search(list, item):
    """
    E.g. Given a list of numbers between 1 and 100, search for an item.

    :param list: A list of integers
    :param item: An integer item
    :return: Returns position of item in list is found, else None
    """

    low = 0
    high = len(list) - 1

    number_of_steps = 0

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            print(number_of_steps)
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

        number_of_steps += 1

    print(number_of_steps)
    return None


# Sample List
sample_list = list(range(1, 100))
# item
sample_item = 76

print(binary_search(list=sample_list, item=sample_item))
