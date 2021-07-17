from linearmap import Map, _MapEntry, _MapIterator

def main():
    students_info = Map()
    students_info.add(10015, "Smith\nJohn\n14 East Main St\n" + \
                             "Somewhere\nVA\n99155")
    students_info.add(10142, "Roberts\nSusan\n231 Quarry Rd\n" + \
                             "Nowhere\nTX\n11133")
    students_info.add(10210, "Brown\nJessica\n231 Quarry Rd\n" + \
                             "Plains\nTN\n30101")
    students_info.add(10175, "Smith\nJane\n81 Jefferson St\n" + \
                             "East End\nPA\n28541")

    print(students_info.valueOf(10210))
    print()
    students_info.remove(10142)
    students_infos = iter(students_info)
    print("Students' Information List")
    print()
    for students_data in students_infos:
        print(students_data.key)
        print(students_data.value)
        print()

main()
