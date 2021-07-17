from linearset import Set, _SetIterator

def main():
    smith = Set()
    smith.add("CSCI-112")
    smith.add("MATH-321")
    smith.add("HIST-340")
    smith.add("ECON-101")

    roberts = Set()
    roberts.add("POL-101")
    roberts.add("ANTH-230")
    roberts.add("CSCI-112")
    roberts.add("ECON-101")

    if smith == roberts:
        print("Smith and Roberts are taking the same courses.")
    else:
        sameCourses = smith.intersect(roberts)
        if len(sameCourses) == 0:
            print("Smith and Roberts are not taking any of " \
                + "the same courses.")
        else:
            print("Smith and Roberts are taking some of the " \
                + "same courses.")
            for course in sameCourses:
                print(course)
        uniqueCourses = smith.difference(roberts)
        if len(uniqueCourses) == 0:
            print("Smith and Roberts are taking the same courses.")
        else:
            print("Smith and Roberts are taking some of the " \
                + "different courses.")
            for course in uniqueCourses:
                print(course)

main()
