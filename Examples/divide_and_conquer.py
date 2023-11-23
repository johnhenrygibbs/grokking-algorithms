# Code for recursive sum function.

def sum(list):

    # The base case is when there are no items left in the array.

    if list == []:
        return 0

    # If there are elements present, use the first number in the list and add it to the sum of the rest of the list.

    return list[0] + sum(list[1:])

    # In Python, a colon on the right side of an index means slice from index 1 to the end of the array.

print(sum([1, 2, 3, 4]))

# Code for counting the number of items on a list recursively.

def count(list):

    # The base case is when there are no items left in the array.

    if list == []:
        return 0

    # If there are elements present, keep a tally by adding 1 to the recursive function call, which shortens the array length each time.

    return 1 + count(list[1:])

print(count([1, 2, 3, 4]))

# Code for finding the maximum number in a list.

def max(list):

    # The base case returns the max number in an array of length 2.

    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]

    # Pass everything to the right of index one back into the max() function until the array satisfies the base case.

    sub_max = max(list[1:])

    return list[0] if list[0] > sub_max else sub_max

print(max([1, 2, 3, 4]))