import sqlite3
import random
import numpy as np
import matplotlib.pyplot as plt
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

def ChangeToGene(x):
    Genes = {}
    for i in range(len(x)):
        Genes[i] = str(x[i]['ID']) + " "
        Genes[i] = Genes[i] + x[i]['Day'] + " "
        if x[i]['Time'] == '8:00-9:00':
            Genes[i] = Genes[i] + "0"
        if x[i]['Time'] == '9:00-10:00':
            Genes[i] = Genes[i] + "2"
        if x[i]['Time'] == '10:00-11:00':
            Genes[i] = Genes[i] + "4"
        if x[i]['Time'] == '11:00-12:00':
            Genes[i] = Genes[i] + "6"
        if x[i]['Time'] == '12:00-13:00':
            Genes[i] = Genes[i] + "8"
        if x[i]['Time'] == '13:00-14:00':
            Genes[i] = Genes[i] + "10"
        if x[i]['Time'] == '14:00-15:00':
            Genes[i] = Genes[i] + "12"
        if x[i]['Time'] == '15:00-16:00':
            Genes[i] = Genes[i] + "14"
        if x[i]['Time'] == '16:00-17:00':
            Genes[i] = Genes[i] + "16"
        if x[i]['Time'] == '17:00-18:00':
            Genes[i] = Genes[i] + "18"
        if x[i]['Time'] == '18:00-19:00':
            Genes[i] = Genes[i] + "20"
        if x[i]['Time'] == '19:00-20:00':
            Genes[i] = Genes[i] + "22"
        if x[i]['Time'] == '20:00-21:00':
            Genes[i] = Genes[i] + "24"
        if x[i]['Time'] == '8:00-9:30':
            Genes[i] = Genes[i] + "1"
        if x[i]['Time'] == '9:30-11:00':
            Genes[i] = Genes[i] + "3"
        if x[i]['Time'] == '11:00-12:30':
            Genes[i] = Genes[i] + "5"
        if x[i]['Time'] == '12:30-14:00':
            Genes[i] = Genes[i] + "7"
        if x[i]['Time'] == '14:00-15:30':
            Genes[i] = Genes[i] + "9"
        if x[i]['Time'] == '15:30-17:00':
            Genes[i] = Genes[i] + "11"
        if x[i]['Time'] == '17:00-18:30':
            Genes[i] = Genes[i] + "13"
        if x[i]['Time'] == '18:30-20:00':
            Genes[i] = Genes[i] + "15"
        if x[i]['Time'] == '20:00-21:30':
            Genes[i] = Genes[i] + "17"
        if x[i]['Time'] == '8:00-11:00':
            Genes[i] = Genes[i] + "024"
        if x[i]['Time'] == '11:00-14:00':
            Genes[i] = Genes[i] + "6810"
        if x[i]['Time'] == '14:00-17:00':
            Genes[i] = Genes[i] + "121416"
    return Genes

def CheckBreak(genes):
    Break = 0
    a = np.zeros(30)
    MaxEven = MaxOdd = -1000
    MinEven = MinOdd = 1000
    for i in range(len(genes)):
        gene1 = genes[i].split(' ')
        if gene1[2] == "024":
            a[0] = 1
            a[2] = 1
            a[4] = 1
            if 4 > MaxEven:
                MaxEven = 4
            if 0 < MinEven:
                MinEven = 0
        elif gene1[2] == "6810":
            a[6] = 1
            a[8] = 1
            a[10] = 1
            if 10 > MaxEven:
                MaxEven = 10
            if 6 < MinEven:
                MinEven = 6
        elif gene1[2] == "121416":
            a[12] = 1
            a[14] = 1
            a[16] = 1
            if 16 > MaxEven:
                MaxEven = 16
            if 12 < MinEven:
                MinEven = 12
        else:
            a[int(gene1[2])] = 1

    for i in range(len(genes)):
        gene2 = genes[i].split(' ')
        if gene2[2] != "024" and gene2[2] != "6810" and gene2[2] != "121416":
            if int(gene2[2]) % 2 == 0 and a[int(gene2[2])] == 1:
                if int(gene2[2]) > MaxEven:
                    MaxEven = int(gene2[2])
                if int(gene2[2]) < MinEven:
                    MinEven = int(gene2[2])
            if int(gene2[2]) % 2 == int(1) and a[int(gene2[2])] == int(1):
                if int(gene2[2]) > MaxOdd:
                    MaxOdd = int(gene2[2])
                if int(gene2[2]) < MinOdd:
                    MinOdd = int(gene2[2])
    if MinEven != 1000:
        for j in range(MinEven, MaxEven + 1, 2):
            if (int(a[j]) == 0):
                Break += 1
    if MinOdd != 1000:
        for jj in range(MinOdd, MaxOdd + 1, 2):
            if (int(a[jj]) == 0):
                Break += 1
    print("Breaks are = " +str(Break))
    return int(Break)



Genes = ChangeToGene(CoursesToRegister1)

parent1 = ['20141 MW 5', '11206 MW 7', '31311 M 7', '20200 MW 13', '31151 M 9', '31151 STU 6']
parent2 = ['11253 M 024', '20132 STUTH 8', '31261 STU 6', '31151 M 9', '20134 W 9', '20233 S 10']
