# Implementation of the linear search on an unsorted sequence.
def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        # If the target is in the ith element, return True
        if theValues[i] == target:
            return True
    return False    # If not found, return False.

# Implementation of the linear search on an sorted sequence.
def sortedLinearSearch(theValues, item):
    n = len(theValues)
    for i in range(n):
        # If the target is found in the ith element, return True
        if theValues[i] == item:
            return True
        # If the target is larger than the ith element, it's not in the sequence.
        elif theValues[i] > item:
            return False
    return False    # The item is not in the sequence.

# Searching for the smallest value in an unsorted sequence.
def findSmallest(theValues):
    n = len(theValues)
    # Assume the first item is the smallest value.
    smallest = theValues[0]
    # Determine if any other item in the sequence is smaller.
    for i in range(n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest     # Return the smallest found.

# Testing the Linearsearch methods.
def main():
    import random
    num_counts = random.randint(1, 10)
    num_list = []
    for _ in range(num_counts):
        num_list.append(random.randint(1, 50))
    print("Num list: ", num_list)
    print("First search")
    print(linearSearch(num_list, 26))
    print("Second search")
    print(sortedLinearSearch(sorted(num_list), 18))
    print("Smallest values:", end=' ')
    print(findSmallest(num_list))

main()
