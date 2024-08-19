# Attendance Tracking System

#### Video Demo: <https://youtu.be/lqaIuvgBYhE>

#### Description:

This Project is Attendance tracking system developed with the aims to bridge the gap caused by paper-based systems in education. with this system teachers can monitor student attendance data efficentely. The system was designed to accurately track the attendance of students in an efficient manner. the system has included different feature onit to make student monitoring process more accurate and reduce errors.

# folder structure

the system has different python files and folders that does different things.
these are:

1. _project.py_ this file is the main file of the system found in root folder.
2. _test_project.py_ this file is test file found in root folder. thes test file test project.py file.
3. _requirements.txt_ this is a text file also found in root folder.
4. _attendanceFile_ this is a folder in the root directory holds _csv_ files.
5. _studentList_ this is a folder in the root directory holds _csv_ files.
6. _README.md_ readme file explain every thing about the project. found in root folder.

## what each file and folder does

### _project.py_

this attendance monitoring system have different feaures to make the job easy. in this file there are about 14 function and each of them has unique responsiblities.

#### functions in project.py file

1.  _registerStudents()_
    this function is used to make a list of students
    the user enter only students name and the function make a list with roll number name date attendance column by itself and save it.
2.  _chooseFile()_
    open the students.csv file and copy data to students list
3.  _writeToFile()_
    open file and write the list data in to csv file
4.  _addDate()_
    add the current Date.
5.  _registerAttendanceInformation()_
    prompt the user to gave student list file and check it and give it to fillAttendance function
6.  _fillAttendance()_
    fill the attendance value [p,a,e] into the dated student list and return the new filled list and the file name user gave
7.  _appendAttendanceValue()_
    append the attendance value into studentList attendance column
8.  _checkFileName()_
    check the file name user give to attendance file if it is duplicated it is not valid and reprompt the user
9.  _previousAttendance()_
    this function give us the list of privious Attendace file
10. _deleteFile()_
    delete the file in the that is the return of deleteChoose function
11. _deleteChoose()_
    prompt the user to enter the folder weather it is students list file or attendance file and return folder path to deleteFile function
12. _menu()_
    used to display the menu.
13. _displayMenu()_
    have a capablity of keeping user in the system until the user wants to exit.

### test_project.py

this file has three functions on it.used to test three of function in project.py file.

1. test_previousAttendance()
   this function test that the previousAttendance function works as expected in the case where the attendance folder is missing.
2. test_deleteChoose()
   check if the deleteChose function return None if their is no folder
3. test*displayMenu()
   The test verifies that the displayMenu function responds correctly to this input by producing an exit message which is *"Program Exited"\_.

### _requirements.txt_

text file found in root folder.
in this text file there is a list of pip installable libraries used in this system.

### _attendanceFile_

this is a folder used to hold _csv_ files those fils are holds students attendace mark.
all the four columns [roll, student name, Date, Attendace] are filled.

### _studentList_

this is a folder used to hold _csv_ files those fils are holds students roll number and student name. this files prepared to filled attendance mark.

### project.py file has some core functionalityes

#### making student list

to monitor students attendance data first their must be students list. The list has column named roll number ,student name , date , attendace. On this feature of making students list user prompted to enter only students name.Then the system turns the input data which means students name and make correctly formatted list. The newly formatted list will have four columns. Named

_roll_ :- which is automatically given by the system to identifie the student uniquley and it increments as the new student created.

_student name_ :- which is the name of students.

_date_ :- column used to hold the date value and formatted as mm-dd-yyyy.This column will have null value when it is created. The actual data wiil be filled by the system itself when this list is in use which means the day the attendance mark filed date will also be filed.

_Attendance_:- column used to hold attendance mark. The attendance mark filled by the user not by the system because of this the user need to fill the attendance mark _carefully_. This column accepte only three type of inputs. Those are **p for present** , **a for absent**, **e for exceused**. Only these inputs are valid another input is not accepted by the system. The user force to enter valid mark by reprompting the input.

After all the columns are prepared correctly the system prompt us weather we want save it or not. If we want to save then it propmts us again to give a file name after that the system save it as a csv file in _\studentList_ folder.

## Tracking attendence data

Tracking student attendance data and storing is main purpose of this system.monitering attendance needs correctly formatted list to fill the attendance mark. After making the list with the four columns listed above the next thing is entering attendance mark for each student.

### There are few steps to start tracking attendace mark

After we choose the start tracking the menu the system gives us a list of _csv_ file and prompt us to enter file name. if the choosen file is exist the system proceed and prompt us to enter valid attendance mark for each student. To finsh tracking save the file as it prompt us to save or not. This fill stored in _\attendanceFile_ folder.

## previous attendance

As the attendance file is stored user can access and watch previous attendance files.

## delete file

User can delete files weather attendace file or student list.

# Modules and Libraries

There is a list python modules and libraries used in this system:

1. sys
2. tabulate
3. pandas
4. os
5. datetime
6. pytest
7. black
8. io
9. patch
10. MagicMock
