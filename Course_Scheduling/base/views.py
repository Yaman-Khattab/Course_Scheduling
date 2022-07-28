from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import random
import numpy as np
import matplotlib.pyplot as plt
from django.db import connection
from .models import Student, Classes, CsCourses
import re

def home(request):
    mydata = Student.objects.all().values()
    courses = []
    for row in mydata:
        courses.append(row['coursesfinished'])
    courses = courses[0].split(',')
    #done1

    FinishedCourses = []
    AllCourse = {}
    h = 0
    for x in courses:
        sqlQury2 = CsCourses.objects.all()
        ss = sqlQury2.filter(courseid = x)
        for yy in sqlQury2:
            AllCourse[h] = {}
            AllCourse[h]['ID'] = yy.courseid
            AllCourse[h]['Name'] = yy.coursename
            AllCourse[h]['Pre'] = yy.prerequisite
            h+=1
        break

    for x in courses:
        sqlQury2 = CsCourses.objects.all()
        ss = sqlQury2.filter(courseid = x)
        for y in ss:
            FinishedCourses.append(y.coursename)

    CoursesToRegister = []
    for i in range(len(AllCourse)):
        if AllCourse[i]['Pre'] == ' ': #AllCourse[i]['Pre'] == '  '
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

    #done2
    tf = []
    sqlQury4 = []
    for i in range(len(CoursesToRegister)):
        sqlcm = Classes.objects.all().values()
        for row in sqlcm:
            if int(row['sectioncapacity']) == int(row['studentregistered']) or str(CoursesToRegister[i]) in courses:
                break
            
            #Stopeed here!


    return render(request,'base/home.html')
