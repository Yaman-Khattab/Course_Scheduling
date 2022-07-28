# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CsCourses(models.Model):
    courseid = models.AutoField(db_column='CourseID', primary_key=True)  # Field name made lowercase.
    coursename = models.TextField(db_column='CourseName', blank=True, null=True)  # Field name made lowercase.
    hours = models.IntegerField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    prerequisite = models.TextField(db_column='Prerequisite', blank=True, null=True)  # Field name made lowercase.
    coursetype = models.TextField(db_column='CourseType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CS_Courses'


class Classes(models.Model):
    coursenumber = models.IntegerField(db_column='CourseNumber',primary_key=True)  # Field name made lowercase.
    coursetitle = models.TextField(db_column='CourseTitle', blank=True, null=True)  # Field name made lowercase.
    sections = models.TextField(db_column='Sections', blank=True, null=True)  # Field name made lowercase.
    day = models.TextField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    sectioncapacity = models.IntegerField(db_column='SectionCapacity', blank=True, null=True)  # Field name made lowercase.
    studentregistered = models.IntegerField(db_column='StudentRegistered', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classes'


class College(models.Model):
    collegeid = models.AutoField(db_column='CollegeID', primary_key=True)  # Field name made lowercase.
    collegename = models.TextField(db_column='CollegeName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'College'


class Student(models.Model):
    stdid = models.AutoField(db_column='StdID', primary_key=True)  # Field name made lowercase.
    stdname = models.TextField(db_column='StdName', blank=True, null=True)  # Field name made lowercase.
    stdmajor = models.TextField(db_column='StdMajor', blank=True, null=True)  # Field name made lowercase.
    gpa = models.TextField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    hoursfinished = models.IntegerField(db_column='HoursFinished', blank=True, null=True)  # Field name made lowercase.
    coursesfinished = models.TextField(db_column='CoursesFinished', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student'
