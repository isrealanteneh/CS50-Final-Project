import sys
import os
import csv
from tabulate import tabulate
from datetime import datetime


attendanceData = []
attendanceData = ["Attendance"]
attendanceFolder = "./attendanceFile"
studentListFolderPath = "./studentList"
data = datetime.now()
currentDate = data.strftime("%d-%m-%y")


def main():
    displayMenu()


# this function is used to make a list of students
# the user enter only students name and the function make a list with roll number name date attendance  column by itself and save it
def registerStudents(folderPath):
    registeredStudentsList = [["Roll number", "Student name", "Date", "Attendance"]]
    print("\nThe attendance list will be formatted as follows: [Roll number, Student name, Date, Attendance]\n")
    studentName = input("Please enter student name 1: ").strip()
    roll = 2
    registeredStudentsList.append([1, studentName, "", ""])
    while True:
        try:
            studentName = input(f"{roll}, ").strip()
            if studentName != "":
                registeredStudentsList.append([roll, studentName, "", ""])
                roll += 1
            else:
                print("student name is empty")
        except KeyboardInterrupt:
            print("\n")
            break
    table = tabulate(registeredStudentsList, headers="firstrow", tablefmt="grid")
    userChoice = input("Do you want to save the list? (Y/N): ") 
    if userChoice.lower() == "y":
        if os.path.exists(folderPath):
            fileName = checkFileName(folderPath)
            return registeredStudentsList, fileName
        else:
            print("Folder path does not exist")

    else:
        return None


# open the students.csv file and copy data to students list
def chooseFile(studentFile):
    students = []
    with open(f"{studentListFolderPath}/{studentFile}", "r") as readCsv:
        studentData = csv.reader(readCsv)
        for row in studentData:
            students.append(row)
        return students


def writeToFile(writtenList, folderPath, fileName):
    with open(f"{folderPath}/{fileName}.csv", "w", newline="") as writeCsv:
        writeFile = csv.writer(writeCsv)
        writeFile.writerows(writtenList)
    print("File saved successfully")


# append the date to date columns
def addDate(studentList):
    for i in studentList:
        if i[2] == "Date":
            i[2] = "Date"
        else:
            i[2] = currentDate
    return studentList


# prompt the user to gave student list file and check it and give it to fillAttendance function
def registerAttendanceInformation():
    print("====== List of students file ======")
    if os.path.exists(studentListFolderPath):
        files = os.listdir(studentListFolderPath)
        for i in range(len(files)):
            print(f"{i+1}, {files[i]}")
        studentFile = input("\nPlease enter the name of the student file to start tracking attendance: ")
        openFile = f"{studentFile}.csv"
        if openFile in files:
            choosenStudentsFile = chooseFile(openFile)
            datedList = addDate(choosenStudentsFile)
            listData, fileName = fillAttendance(datedList)
            return listData, fileName
        else:
            print("File name is not correct")


# fill the attendance value [p,a,e] into the dated student list and return the new filled list and the file name user gave
def fillAttendance(datedList):
    print(
        "To mark attendance, enter:\n'P' for present\n'A' for absent\n'E' for excused\nInvalid entries will not be accepted: "
    )
    print(f"Today it is {currentDate} ")  # print the date today
    for i in range(len(datedList)):
        if i == 0:
            pass
        else:
            # printing the role and the name of student only to user
            attnedance = input(f"{datedList[i][0]}, {datedList[i][1]}: ")
            while True:
                # if the input is only p, e, a it can be valid input
                if attnedance.lower() in ["p", "a", "e"]:
                    attendanceData.append(attnedance)
                    break
                else:
                    attnedance = input(f"Please enter the correct value ")
    try:
        studentsList, fileName = appendAttendanceValue(attendanceData, datedList)
        writeToFile(studentsList, attendanceFolder, fileName)
        return studentsList, fileName
    except TypeError as te:
        print("File not saved", te)


# append the attendance value into studentList attendance column
def appendAttendanceValue(attendanceValue, studentList):
    for i in range(len(attendanceValue)):
        try:
                if studentList[i] == 0:
                        attendanceValue[i] = "Attendance"
                else:
                        studentList[i][3] = attendanceValue[i]
                table = tabulate(studentList, headers="firstrow", tablefmt="grid")
        except IndexError: print("The selected student list file is empty.")
    print(table)
    wantToSave = input("Would you like to save this data? (Y/N): ") 

    if wantToSave.lower() == "y":
        fileName = checkFileName(attendanceFolder)
        return studentList, fileName


# check the file name user give to attendance file if it is duplicated it is not valid and reprompt the user
def checkFileName(folderPath):
    fileName = input("Enter file name: ")
    if os.path.exists(folderPath):
        files = os.listdir(folderPath)
        fileNames = []
        for file in files:
            # append file name only with out its extention to fileNames list
            fileNames.append(file.split(".")[0])
        while True:
            if fileName not in fileNames:
                return fileName
            else:
                fileName = input(
                    "File name exists. Enter a new name:"

                ).strip()


# this function give us the list of privious Attendace file
def previousAttendance():
    print("List of previous attendance")
    if os.path.exists(attendanceFolder):
        files = os.listdir(attendanceFolder)
        for i in range(len(files)):
            print(f"{i+1}, {files[i]}")
        fileName = input("Enter file name to view: ")
        ViewFile = f"{fileName}.csv"
        viewList = []
        for file in files:
            if ViewFile == file:
                # open the neede file in the attendance folder and open the file to view
                try:
                    with open(f"{attendanceFolder}/{ViewFile}", "r") as readFile:
                        readAttendanceData = csv.reader(readFile)
                        for line in readAttendanceData:
                            # if the file exist append it in to viewList list
                            viewList.append(line)
                        table = tabulate(viewList, headers="firstrow", tablefmt="grid")
                        print(table)
                except FileNotFoundError:
                    print("File not found")
        if viewList == []:
            print(" No such file name")


# delete the file in the that is the return of deleteChoose function
def deleteFile():
    deleteFolder = deleteChoose()
    if deleteFolder != None:
        try:
                studentFile = os.listdir(deleteFolder)
                roll = 1
              
                for file in studentFile:
                        print(f"{roll}, {file}")
                        roll += 1
                fileName = input("Enter the file name to delete: ")
                file = f"{fileName}.csv"
                if file in studentFile:
                    os.remove(f"{deleteFolder}/{file}")
                    print("file deleted")
                else:
                                print(f"{file} does not exist")
        except Exception:
                print(" No such file or directory")
    else:print("Invalid input")


# prompt the user to enter the folder weather it is students list file or attendance file and return folder path to deleteFile function
def deleteChoose():
   print("Enter the number corresponding to the file you want to delete:")
   print("1. Students list file")
   print("2. Attendance file")
   print("(Please confirm your choice before proceeding)")
   deleteChoise = input(": ")
   if deleteChoise == "1":
        return studentListFolderPath
   elif deleteChoise == "2":
        return attendanceFolder
   else:
        return None


def menu():
    print("\n ======= Welcome to student attendance tracking system ====== \n")
    print("1, Add student list ")
    print("2, Start tracking ")
    print("3, Previous attendance ")
    print("4, Delete file \n")
    userChoise = input("Enter choise: ")
    if userChoise == "1":
        try:
            studentList, fileName = registerStudents(studentListFolderPath)
            writeToFile(studentList, studentListFolderPath, fileName)
        except:
            print("File not saved")
    elif userChoise == "2":
        registerAttendanceInformation()
    elif userChoise == "3":
        previousAttendance()
    elif userChoise == "4":
        deleteFile()

    else:
        print("Invalid Choice ")
    wantToExit = input("Would you like to continue? (Y/N): ")
    return wantToExit.lower().strip()


def displayMenu():
    exitChoise = menu()
    while True:
        if exitChoise == "n":
            print("Program Exited")
            break
        else:
            exitChoise = menu()


if __name__ == "__main__":
    main()
