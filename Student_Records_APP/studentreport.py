# Produces a student report from data extracted from an external source.
import sys
sys.path.append("H:\DS_and_Algorithms_summary\Student_Records_APP\Student_File_Reader_ADT")
from studentfile import StudentFileReader

# Name of the file to open
FILE_NAME = "students.txt"

def main():
    # Extract the student records from the given text file.
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    studentList = reader.fetchAll()
    reader.close()

    # Sort the list by id number. Each object is passed to the lambda
    # exporession which returns the idNum field of the object.
    studentList.sort(key=lambda rec: rec.idNum)

    # Print the student report
    printReport(studentList)

# Prints the student report.
def printReport(theList):
    # The class names associated with the class codes.
    classNames = (None, "Freshman", "Sophomore", "Junior", "Senior")

    # Print the header
    print("LIST OF STUDENTS".center(50))
    print("")
    print("%-5s    %-25s    %-10s   %-4s" % ('ID', 'NAME', 'CLASS', 'GPA'))
    print("%5s    %25s    %10s   %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))
    # Print the body
    for record in theList:
        print("%5d    %-25s   %-10s    %4.2f" % \
                        (record.idNum, \
                         record.lastName + ', ' + record.firstName, \
                         classNames[record.classCode], record.gpa))
    # Add a footer
    print("-" * 55)
    print("Number of students:", len(theList))

# Executes the main routine
main()
