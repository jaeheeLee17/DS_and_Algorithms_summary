from linearbag import Bag, _BagIterator

def main():
    myBag = Bag()
    items = [19, 74, 23, 19, 12]
    for item in items:
        myBag.add(item)
    iterator = myBag.__iter__()
    while True:
        try:
            item = iterator.__next__()
            print(item)
        except StopIteration:
            print("There aren't any items in the bag.")
            break

main()
