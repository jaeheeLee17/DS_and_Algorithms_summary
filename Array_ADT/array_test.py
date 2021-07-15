# Fill a 1-D array with random values, then print item, one per line.
from array_structure import Array, _ArrayIterator
import random

def main():
    # The constructor is called to create the array.
    valueList = Array(100)
    for i in range(len(valueList)):
        valueList[i] = random.random()

        # Print the values, one per line.
    for value in valueList:
        print(value)

# Execute the main routine.
main()
