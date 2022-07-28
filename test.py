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
# Check if the ID Given is an optional course or Compulsory Program Requirement
def CheckOptional(IDs):
    for i in range(len(CoursesToRegister1)):
        if str(IDs) == str(CoursesToRegister1[i]['ID']) and (CoursesToRegister1[i]['CourseType'] == "Elective University Requirements (Scientific, Practical)" or CoursesToRegister1[i]['CourseType'] == "Elective University Requirements (General)" or CoursesToRegister1[i]['CourseType'] == "Compulsory University Requirements"):
            return 1
    return 0

# Changing the format of the dataset(Courses) so the genetic algorithm could be easily process it.
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

def CheckRestrictions(genes):
    sum = 0
    for i in range(len(genes) - 1):
        gene1 = genes[i].split(' ')
        for j in range(i + 1, len(genes)):
            gene2 = genes[j].split(' ')

            if ((gene2[1] in gene1[1]) or (gene1[1] in gene2[1])) and (gene2[2] == gene1[2]):
                sum = sum + 1

            if len(gene1[2]) >= 3:
                if gene1[2] == "024":
                    if "0" == gene2[2] or "2" == gene2[2] or "4" == gene2[2] or "1" == gene2[2] or "3" == gene2[2]:
                        sum = sum + 1
                if gene1[2] == "6810":
                    if "6" == gene2[2] or "8" == gene2[2] or "10" == gene2[2] or "5" == gene2[2] or "7" == gene2[2]:
                        sum = sum + 1
                if gene1[2] == "121416":
                    if "12" == gene2[2] or "14" == gene2[2] or "16" == gene2[2] or "9" == gene2[2] or "11" == gene2[2]:
                        sum = sum + 1

            if len(gene2[2]) >= 3:
                if gene2[2] == "024":
                    if "0" == gene1[2] or "2" == gene1[2] or "4" == gene1[2] or "1" == gene1[2] or "3" == gene1[2]:
                        sum = sum + 1
                if gene2[2] == "6810":
                    if "6" == gene1[2] or "8" == gene1[2] or "10" == gene1[2] or "5" == gene1[2] or "7" == gene1[2]:
                        sum = sum + 1
                if gene2[2] == "121416":
                    if "12" == gene1[2] or "14" == gene1[2] or "16" == gene1[2] or "9" == gene1[2] or "11" == gene1[2]:
                        sum = sum + 1

    return sum

def CheckUniqueness(genes):
    sum = 0
    for i in range(len(genes) - 1):
        gene1 = genes[i].split(' ')
        for j in range(i + 1, len(genes)):
            gene2 = genes[j].split(' ')
            if (gene1[0] == gene2[0]):
                sum = sum + 1
    return sum

def Fitness(sch1, hour, Days, Break):
    d = 0.0
    numOptional = 0.0
    if CheckUniqueness(sch1) >= 1:
        d = d + (CheckUniqueness(sch1) * 0.5)

    if CheckRestrictions(sch1) >= 1:
        d = d + (CheckRestrictions(sch1) * 0.5)

    if CheckBreak(sch1) > Break:
            d = (d + 0.1) + (CheckBreak(sch1) * 0.2)
    
    if CheckHours(sch1, hour) == -1:
        d = d + 0.5
    if Days != "everyday":
        if CheckDays(sch1, Days) >= 1:
            d = d + (CheckDays(sch1, Days) * 0.6)

    for i in range(len(sch1)):
        gene1 = sch1[i].split(' ')
        numOptional = numOptional + int(CheckOptional(gene1[0]))
    if numOptional > optional_courses:
        d = d + (numOptional * 0.2)
    fitness = 1 / (d + 1)
    return fitness

def Crossover(x1,x2):
    holder = []
    for h in x1:
        holder.append(h)
    for gh in x2:
        holder.append(gh)
    random.shuffle(holder)
    return holder
def Mutation(x1, Days):
    if Days != "everyday":
        num1 = 0
        for i in range(len(x1)):
            num1 = i
            gene2 = x1[i].split(" ")
            if gene2[1] not in Days:
                break
        num2 = random.randint(0, len(Genes)-1)
        gene1 = Genes[num2].split(" ")
        while gene1[1] not in Days and gene1 not in x1:
            num2 = random.randint(0, len(Genes) - 1)
            gene1 = Genes[num2].split(" ")
        x1[num1] = Genes[num2]
        return x1
    if Days == "everyday":
        num1 = random.randint(0,len(x1)-1)
        num2 = random.randint(0, len(Genes)-1)
        x1[num1] = Genes[num2]
        return x1

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
    return int(Break)

def CheckHours(x1, hour):
    sum = 0
    for i in range(len(x1)):
        gene1 = x1[i].split(" ")
        for j in range(len(CoursesToRegister1)):
            if str(gene1[0]) == str(CoursesToRegister1[j]['ID']):
                sum = sum + int(CoursesToRegister1[j]['Hours'])
                break

    if sum == hour:
        return 1
    else:
        return -1

def CheckDays(x1, x2):
    sum = 0
    for i in range(len(x1)):
        gene1 = x1[i].split(' ')
        if gene1[1] not in x2:
            sum = sum + 1
    return sum

CoursesToRegister1 = Preparing()
Genes = ChangeToGene(CoursesToRegister1)

# Student will enter the specification of the schedule:
Days = "everyday"
Hours = 18
Break = 1 # The value Specified is Up to 
optional_courses = 2  # The value Specified is Up to 

# Every Parent1 contain a schedule and vise versa for parent2
parent1 = []
parent2 = []
Population = []
AllFitness = []
MaxFitness = 0.0
Iterations = 1

num_of_courses = int((Hours / 3)) + (Hours % 3)


while len(parent1) != num_of_courses:
    num1 = random.randint(0, len(Genes)-1)
    parent1.append(Genes[num1])
    if CheckUniqueness(parent1) >= 1 or CheckRestrictions(parent1) >= 1:
        parent1.pop()

while len(parent2) != num_of_courses:
    num1 = random.randint(0, len(Genes)-1)
    parent2.append(Genes[num1])
    if CheckUniqueness(parent2) >= 1 or CheckRestrictions(parent2) >= 1:
        parent2.pop()
print("Main Parent1 = " +str(parent1))
print("Main Parent2 = " + str(parent2)) 
Population.append(parent1)
Population.append(parent2)
AllFitness.append(format(Fitness(Population[0], Hours, Days, Break), ".2f"))
AllFitness.append(format(Fitness(Population[1], Hours, Days, Break), ".2f"))


bs = 0
while Iterations != 200:
    child1 = []
    child2 = []
    print("Chromosome1 " + str(bs) + ": " + str(format(Fitness(parent1, Hours, Days, Break), ".2f")) + "\n")
    print("Chromosome2 " + str(bs+1) + ": " + str(format(Fitness(parent2, Hours, Days, Break), ".2f")) + "\n")
    #print("Parent 1 = " + str(parent1))
    #print("Parent 2 = " + str(parent2))
    bs = bs + 2
    holder = Crossover(parent1, parent2)
    #print("Holder is:" + str(holder))
    s = int(len(parent1))

    for j in range(0, int(len(parent1))):
        child1.append(holder[j])
        child2.append(holder[s])
        s += 1

    #print("Before Mutation")
    #print("Child 1 = " + str(child1))
    #print("Child 2 = " + str(child2))

    child1 = Mutation(child1, Days)
    child2 = Mutation(child2, Days)
    #print("After Mutation:")
    #print("Child 1 = " + str(child1))
    #print("Child 2 = " + str(child2))
    Population.append(child1)
    Population.append(child2)

    for i in range(Iterations*2, len(Population)):
        AllFitness.append(format(Fitness(Population[i], Hours, Days, Break), ".2f"))
    output = sorted(AllFitness, key=float)

    if float(output[-1]) > float(MaxFitness):
        MaxFitness = output[-1]

    for i in range(len(Population)):
        if output[-1] == format(Fitness(Population[i], Hours, Days, Break), ".2f"):
            parent1 = Population[i]
        if output[-2] == format(Fitness(Population[i], Hours, Days, Break), ".2f"):
            parent2 = Population[i]

    Iterations = Iterations + 1

STUTH = []
MW = []
everyday = []

for i in range(len(Population)):
    x = format(Fitness(Population[i], Hours, Days, Break), ".2f")
    if float(x) == float(1.00):
        if CheckDays(Population[i], "STUTH") == 0:
            STUTH.append(Population[i])
        elif CheckDays(Population[i], "MW") == 0:
            MW.append(Population[i])
        else:
            everyday.append(Population[i])

print("\n\nschedules for Sunday, Tuesday, Thursday: \n")
for j in range(len(STUTH)):
    print(STUTH[j])

print("\n\nschedules for Monday, Wednesday: \n")

finalcourse = []
checkquniquness = []
for j in range(len(MW)):
    print(MW[j])
    finalcourse1 = []
    test1 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
             "", "", "", "", "", "", "", "", "", "", ""]
    for count in MW[j]:
        new_courses = count.split(" ")
        test1[int(new_courses[2])] = count
    for ff in test1:
        if ff != "":
            finalcourse1.append(ff)
    finalcourse.append(finalcourse1)

for i in range(0, len(finalcourse)):
        if finalcourse[i] not in checkquniquness:
            checkquniquness.append(finalcourse[i])
print("Unique Courses are:")
for xx in checkquniquness:
    print(xx)


print("\n\nschedules for Everyday: \n")
for j in range(len(everyday)):
    print(everyday[j])

xx = []
fit = sorted(AllFitness, key=float)
for i in range(len(AllFitness)):
    xx.append(i)
print(len(Population))
plt.plot(xx, fit)
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title("All Fitness")
plt.show()
