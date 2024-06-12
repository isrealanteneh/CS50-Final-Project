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
                openFile = input("\n Enter students file name with it's extenstion to Track Attendance: ")
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
              
def checkFileName(folderPath):
         fileName = input("Enter file name: ")
         if os.path.exists(folderPath):
                        files = os.listdir(folderPath)
                        fileNames = []
                        for file in files:
                                fileNames.append(file.split(".")[0])
                        
                        while(True):
                                if fileName not in  fileNames:
                                        return  fileName
                                else:
                                        fileName = input("file name already exists please enter new name: ").strip()


def previousAttendance():
        print("List of previous attendance")
        if os.path.exists(attendanceFolder):
                files  = os.listdir(attendanceFolder)
                for i in range(len(files)):
                        print(f"{i+1}, {files[i]}")
                openFile = input("Enter file name with it's extenstion to view: ")
                viewList = []
                for file in files:
                        if openFile == file:
                                with open(f'./attendanceFile/{openFile}', 'r') as readFile:
                                        readAttendanceData = csv.reader(readFile)
                                        for line in readAttendanceData:
                                                viewList.append(line)
                                        
                                        table = tabulate(viewList,headers='firstrow', tablefmt='grid')
                                        print(table)
                if viewList ==  []:
                                print(" No such file name")
                                

def menu():
        print("\n ======= Welcome to student attendance tracking system ====== \n")
        print("1, Add student list ")
        # print("2, check student list")
        print("2, Start tracking ")
        print("3, Previous attendance ")
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