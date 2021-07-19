# Implementation of the Set ADT container using a Python list.
class Set:
    # Creates an empty set instance.
    def __init__(self):
        self._theElements = list()

    # Returns the number of items in the set
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(item)

    # Determines if two sets are equal
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            # return self.isSubsetOf(setB)
            for i in range(len(self)):
                if self._theElements[i] != setB._theElements[i]:
                    return False
            return True

    # Determines if this set is a subset of setB
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    # Creates a new set from the union of this set and setB
    def union(self, setB):
        '''
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet
        '''
        newSet = Set()
        a, b = 0, 0
        # Merge the two lists together until one is empty.
        while a < len(self) and b < len(setB):
            valueA = self._theElements[a]
            valueB = self._theElements[b]
            if valueA < valueB:
                newSet._theElements.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet._theElements.append(valueB)
                b += 1
            else:   # Only one of the two duplicates are appended.
                newSet._theElements.append(valueA)
                a += 1
                b += 1
        # If listA contains more items, append them to newList
        while a < len(self):
            newSet._theElements.append(self._theElements[a])
            a += 1
        # Or if listB contains more items, append them to newList
        while b < len(setB):
            newSet._theElements.append(setB._theElements[b])
            b += 1
        return newSet

    # TODO: Creates a new set from the intersection: self set and setB.
    def intersect(self, setB):
        newSet = Set()
        for element in setB:
            if element in self:
                newSet._theElements.append(element)
        return newSet

    # TODO: Creates a new set from the difference: self set and setB.
    def difference(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element in self:
                newSet._theElements.remove(element)
        return newSet

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)

    # Finds the position of the element within the ordered list..
    def _findPosition(self, element):
        start = 0
        end = len(self) - 1
        while start <= end:
            mid = (start + end) // 2
            if self[mid] == element:
                return mid
            elif element < self[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start

# An iterator for the Set ADT.
class _SetIterator:
    def __init__(self, theElements):
        self._SetRef = theElements
        self._curidx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curidx < len(self._SetRef):
            entry = self._SetRef[self._curidx]
            self._curidx += 1
            return entry
        else:
            raise StopIteration
