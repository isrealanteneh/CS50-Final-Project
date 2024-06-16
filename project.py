import sys
import os
import csv
from tabulate import tabulate
from datetime import datetime


attendanceData = []
attendanceData = ["Attendance"]
attendanceFolder = "./attendanceFile"
studentListFolderPath = "./studentList"

def main():
       displayMenu()


def registerStudents(folderPath):
    registeredStudentsList = [["Roll number","Student name","Date", "Attendance"]]
    studentName = input("Please enter student name 1: ").strip()
    roll = 2
    registeredStudentsList.append([1, studentName,"",""])
    while(True):
        try:
            studentName = input(f"{roll} : ").strip()
            if studentName != "":
                registeredStudentsList.append([roll, studentName,"",""])
                roll += 1
            else:print("student name is empty")
        except KeyboardInterrupt:
            print("\n")
            break
    table = tabulate(registeredStudentsList,headers='firstrow',tablefmt='grid')
    userChoice = input("want to save or not the list enter (Y/N): ")
    if(userChoice.lower() == "y"):
         if(os.path.exists(folderPath)):
                fileName = checkFileName(folderPath)
                return registeredStudentsList , fileName
         else:print("Folder path does not exist")

    else: return None

# open the students.csv file and copy data to students list

def chooseFile(studentFile):
        students = []
        with open(f'{studentListFolderPath}/{studentFile}', 'r') as readCsv:
                studentData = csv.reader(readCsv)
                for row in studentData:
                        students.append(row)
                return students


def writeToFile(writtenList,folderPath ,fileName):         
         with open(f'{folderPath}/{fileName}.csv', 'w',  newline='') as writeCsv:
                writeFile = csv.writer(writeCsv)
                writeFile.writerows(writtenList)
         print("File saved successfully")


# append the date to date columns
def addDate(studentList):
        data = datetime.now()
        currentDate = data.strftime('%d-%m-%y')
        for i in studentList:
                if i[2] == "Date": i[2] = 'Date'
                else: i[2] = currentDate
        return studentList



def registerAttendanceInformation():
        data = datetime.now()
        currentDate = data.strftime('%d-%m-%y')  
        print("====== List of students file ======")
        if os.path.exists(studentListFolderPath):
                files  = os.listdir(studentListFolderPath)
                for i in range(len(files)):
                        print(f"{i+1}, {files[i]}")
                studentFile = input("\n Enter students file name to Track Attendance: ")
                openFile = "f{studentFile}.csv"
                if openFile in files:
                       choosenStudentsFile = chooseFile(openFile)
                       datedList = addDate(choosenStudentsFile)
                else:print("File name is not correct") 

        print('\n ====== Input \'P\' for present \'a\' for absent \'e\' for excuse other inputs are not valid ====== ')
        print(f"Today it is {currentDate} ")
       
        for i in range(len(datedList)):
                if i == 0: pass
                else:
                        attnedance = input(f"{datedList[i][0]}, {datedList[i][1]}: ")
                        while (True):
                                # if the input is only p, e, a it can be valid input
                                if (attnedance.lower() in ['p','a','e']):
                                        attendanceData.append(attnedance)
                                        break
                                else:attnedance = input(f"Please inter correct value : ")
        try:
                studentsList,fileName = appendAttendanceValue(attendanceData, datedList)
                writeToFile(studentsList,attendanceFolder, fileName)
                return studentsList,fileName
        except TypeError as te: print("File not saved", te)                

# append the attendance value into studentList attendance column
def appendAttendanceValue(attendanceValue,studentList):
        for i in range(len(attendanceValue)):
                if studentList[i] == 0:
                        attendanceValue[i] ="Attendance"
                else: studentList[i][3] = attendanceValue[i]
        table = tabulate(studentList,headers='firstrow',tablefmt='grid')
        print(table)
        wantToSave = input("do you want to save this data (Y/N): ")
        if wantToSave.lower() == 'y':
                fileName = checkFileName(attendanceFolder)
                print(fileName)
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
                        
                        while(True):
                                if fileName not in  fileNames:
                                        return  fileName
                                else:
                                        fileName = input("file name already exists please enter new name: ").strip()

# this function give us the list of privious Attendace file 
def previousAttendance():
        print("List of previous attendance")
        if os.path.exists(attendanceFolder):
                files  = os.listdir(attendanceFolder)
                for i in range(len(files)):
                        print(f"{i+1}, {files[i]}")
                fileName = input("Enter file name to view: ")
                ViewFile = f"{fileName}.csv"
                viewList = []
                for file in files:
                        if ViewFile == file:
                                # open the neede file in the attendance folder and open the file to view
                                try:
                                        with open(f'{attendanceFolder}/{ViewFile}', 'r') as readFile:
                                                readAttendanceData = csv.reader(readFile)
                                                for line in readAttendanceData:
                                                        # if the file exist append it in to viewList list
                                                        viewList.append(line)
                                                table = tabulate(viewList,headers='firstrow', tablefmt='grid')
                                                print(table)
                                except FileNotFoundError:  print("File not found")
                if viewList ==  []:
                                print(" No such file name")

# delete the file in the that is the return of deleteChoose function
def deleteFile():
        deleteFolder = deleteChoose()
        try:
                studentFile = os.listdir(deleteFolder)
                roll = 1
                for file in studentFile:
                        print(f"{roll}, {file}")
                        roll += 1
                fileName = input("enter file name only to delete: ")
                file = f"{fileName}.csv"
                if file in studentFile:
                        # os.remove(file)
                        print("file deleted")
                else: print(f"{file} does not exist")
        except Exception :print(" No such file or directory")                                


# prompt the user to enter the folder wether it is students list file or attendance file and return folder path to deleteFile function 
def deleteChoose():
        print("Enter 1 to delete students list file and 2 to delete attendance file ")
        deleteChoise = input(": ")
        if deleteChoise == "1":
                return studentListFolderPath
        elif deleteChoise == "2":
                return attendanceFolder
        else: return "./"
                

                                          
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
                        writeToFile(studentList,studentListFolderPath, fileName)
                except: print("File not saved")
        elif userChoise == "2":
                registerAttendanceInformation()                              
        elif userChoise == "3":
                previousAttendance()
        elif userChoise == "4":
                deleteFile()

        else: print("Invalid Choice ")
        wantToExit = input("To continue or exit enter (Y/N): ")
        return wantToExit.lower().strip()

def displayMenu():
        exitChoise = menu()
        while(True):
                if exitChoise == "n":
                        print("Program Exited")
                        break
                else: 
                        exitChoise = menu()


if __name__ == "__main__":
        main()