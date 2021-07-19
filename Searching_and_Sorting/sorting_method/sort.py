# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n - 1 bubble operations on the sequence.
    for i in range(1, n):
        # Bubble the largest item to the end.
        for j in range(n - i):
            if theSeq[j] > theSeq[j + 1]:   # swap the j and j + 1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
    return theSeq

# Sorts a sequence in ascending order using selection sort algorithm.
def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        # Swap the ith value and smallNdx value only if the smallest value is
        # not already in its proper position. Some implementations omit testing
        # the condition and always swap the two values.
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    return theSeq

# Sorts a sequence in ascending order using insertion sort algorithm.
def insertionSort(theSeq):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned.
        value = theSeq[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            # Shift the items to the right during the search.
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        # Put the saved value into the open slot.
        theSeq[pos] = value
    return theSeq

# Merges two sorted lists to create and return a new sorted list.
def mergeSortedLists(listA, listB):
    # Create the new lst and initialize the list markers.
    newList = list()
    a, b = 0, 0

    # Merge the two lists together until one is empty.
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
    # If listA contains more items, append them to newList
    while a < len(listA):
        newList.append(listA[a])
        a += 1

    # Or if listB contains more items, append them to newList
    while b < len(listB):
        newList.append(listB[b])
        b += 1

    return newList

# Testing the sorting method.
def main():
    import random
    num_counts = random.randint(1, 10)
    num_list = []
    for _ in range(num_counts):
        num_list.append(random.randint(1, 50))
    print("Num list: ", num_list)
    print("Bubble Sort")
    print(bubbleSort(num_list))
    print("Selection Sort")
    print(selectionSort(num_list))
    print("Insertion Sort")
    print(insertionSort(num_list))
    a_list, b_list = [], []
    a_num, b_num = random.randint(1, 20), random.randint(1, 20)
    for _ in range(a_num):
        a_list.append(random.randint(1, 50))
    for _ in range(b_num):
        b_list.append(random.randint(1, 50))
    print("List A:", a_list)
    print("List B:", b_list)
    print("Merge Sort")
    print(mergeSortedLists(sorted(a_list), sorted(b_list)))

main()
