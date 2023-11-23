# Code for a quicksort() algorithm.

def quicksort(array):

    # Defining our base case as "sorted" arrays with 0 or 1 element.

    if len(array) < 2:
        return array

    # Declare a "pivot" point and compare items in the array against it, placing numbers into less and greater arrays.

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >= pivot]

        # Call quicksort() on the sub arrays and combine them with the pivot point in the middle.

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))