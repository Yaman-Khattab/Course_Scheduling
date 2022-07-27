import sqlite3
import random
import numpy as np
import matplotlib.pyplot as plt
def Preparing():
    try:
        conn = sqlite3.connect('project.db')
        print("opened database successfuly")
    except Exception as e:
        print("Error during connection:", str(e))

    result = conn.execute("SELECT * FROM Student")
    courses = []

    for row in result:
        courses.append(row)
        numCourses = courses[0][5]
        numCourses = numCourses.split(',')

    FinishedCourses = []
    for x in range(len(numCourses)):
        sqlQury2 = conn.execute("select CourseName FROM CS_Courses where CourseID ="+str(numCourses[x])+"")
        for row in sqlQury2:
            for col in row:
                FinishedCourses.append(col)
    AllCourse = {}
    h = 0
    sqlQury3 = conn.execute("select CourseID, CourseName, Prerequisite from CS_Courses")
    for row in sqlQury3:
        AllCourse[h] = {}
        AllCourse[h]['ID'] = row[0]
        AllCourse[h]['Name'] = row[1]
        AllCourse[h]['Pre'] = row[2]
        h+=1

    CoursesToRegister = []
    for i in range(len(AllCourse)):
        if AllCourse[i]['Pre'] == " ":
            CoursesToRegister.append(AllCourse[i]['ID'])
        elif "," in AllCourse[i]['Pre']:
            Prerequisite = AllCourse[i]['Pre'].split(",")
            for j in range(len(Prerequisite)):
                if Prerequisite[j] in FinishedCourses:
                    x+=1
                    if x == len(Prerequisite):
                        CoursesToRegister.append(AllCourse[i]['ID'])
            Prerequisite.clear()
            x = 0
        elif "," not in AllCourse[i]['Pre'] and AllCourse[i]['Pre'] != " ":
            if AllCourse[i]['Pre'] in FinishedCourses:
                CoursesToRegister.append(AllCourse[i]['ID'])

    CoursesToRegister1 = {}
    counter = 0
    for i in range(len(CoursesToRegister)):
        sqlQury4 = conn.execute("select c1.CourseID, c1.CourseName, c1.Hours, c1.Prerequisite, c1.CourseType,"
                                " c2.Day, c2.Time, c2.Sections, c2.SectionCapacity, c2.StudentRegistered from"
                                " CS_Courses c1, Classes c2 where c1.CourseID = "+str(CoursesToRegister[i])+""
                                " and c1.CourseID = c2.CourseNumber")
        for row in sqlQury4:
            if str(CoursesToRegister[i]) in numCourses or int(row[8]) == int(row[9]):
                break
            CoursesToRegister1[counter] = {}
            CoursesToRegister1[counter]['ID'] = row[0]
            CoursesToRegister1[counter]['Name'] = row[1]
            CoursesToRegister1[counter]['Hours'] = row[2]
            CoursesToRegister1[counter]['Pre'] = row[3]
            CoursesToRegister1[counter]['CourseType'] = row[4]
            CoursesToRegister1[counter]['Day'] = row[5]
            CoursesToRegister1[counter]['Time'] = row[6]
            CoursesToRegister1[counter]['Sections'] = row[7]
            CoursesToRegister1[counter]['SectionCapacity'] = row[8]
            CoursesToRegister1[counter]['StudentRegistered'] = row[9]
            counter = counter + 1
    return CoursesToRegister1
CoursesToRegister1 = Preparing()

print(CoursesToRegister1)