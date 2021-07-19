# Implementation of the binary search algorithm.
def binarySearch(theValues, target):
    # Start with the entire sequence of elements.
    start = 0
    end = len(theValues) - 1

    # Repeatedly subdivide the sequence in half until the target is found.
    while start <= end:
        # Find the midpoint of the sequence.
        mid = (start + end) // 2
        # Does the midpoint contain the target?
        if theValues[mid] == target:
            return True
        # Or does the target precede the midpoint?
        elif target < theValues[mid]:
            end = mid - 1
        # Or does the target follow the midpoint?
        else:
            start = mid + 1
    # If the sequence cannot be subdivided further, we're done.
    return False

# Modified version of the binary search that returns the index within
# a sorted sequence indicating where the target should be located.
def findSortedPosition(theList, target):
    start = 0
    end = len(theList) - 1
    while start <= end:
        mid = (start + end) // 2
        if theList[mid] == target:
            return mid  # Index of the target
        elif target < theList[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return low  # Index where the target value should be.

# Testing the Binarysearch methods.
def main():
    import random
    num_counts = random.randint(1, 10)
    num_list = []
    for _ in range(num_counts):
        num_list.append(random.randint(1, 50))
    print("Num list: ", num_list)
    print("Binary search")
    print(binarySearch(num_list, 26))
    print("Target Location")
    print(findSortedPosition(sorted(num_list), 11))

main()
