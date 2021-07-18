import random

def make_test_data(stores, items):
    salesdata_nums = random.randint(1, 50)
    salesdata = []
    for _ in range(salesdata_nums):
        store_num = str(random.randint(1, stores))
        month_num = str(random.randint(1, 12))
        item_num = str(random.randint(1, items))
        sales_amount = str(round(random.random() * 1000, 2))
        salesdata.append([store_num, month_num, item_num, sales_amount])
    return salesdata

def main():
    f = open("sales_data.txt", "w")
    stores = random.randint(1, 5)
    items = random.randint(1, 20)
    result = make_test_data(stores, items)
    stores, items = str(stores), str(items)
    f.write(stores + "\n")
    f.write(items + "\n")
    for unit_data in result:
        for data in unit_data:
            f.write(data + " ")
        f.write("\n")
    print("Write finished")
    f.close()

main()
