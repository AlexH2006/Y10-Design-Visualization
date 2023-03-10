import csv

with open ("API_SE.SEC.ENRR_DS2_en_csv_v2_4672725.csv", newline='') as csvdata:
    reader = csv.reader(csvdata)
    enrollment=list(reader)

with open ("API_SP.POP.0014.TO_DS2_en_csv_v2_4661114.csv", newline='') as csvdata:
    reader=csv.reader(csvdata)
    population=list(reader)

#we open the csv file that we are going to process

income_enrollment=[]

i=1
while i<len(enrollment):   
    if enrollment[i][1]=="HIC" or enrollment[i][1]=="LIC" or enrollment[i][1]=="MIC" or enrollment[i][1]=="UMC" or enrollment[i][1]=="LMC":
        l=[]
        l.append(enrollment[i][0])
        l.append(enrollment[i][1])
        l.append(enrollment[i][2])
        j=14
        while j<len(enrollment[i])-2:
            l.append(enrollment[i][j])
            j+=1
        income_enrollment.append(l)
    i+=1

#the year=index+1967
#We extract the enrollment information based on income level

income_population=[]

i=1
while i<len(population):   
    if population[i][1]=="HIC" or population[i][1]=="LIC" or population[i][1]=="MIC" or population[i][1]=="UMC" or population[i][1]=="LMC":
        l=[]
        l.append(population[i][0])
        l.append(population[i][1])
        l.append(population[i][2])
        j=14
        while j<len(population[i])-2:
            l.append(population[i][j])
            j+=1
        income_population.append(l)
    i+=1

#the year=index+1967
#We extract the enrollment information based on income level.

i=1
while(i<len(income_population)):
    j=3
    while j<len(income_population[i]):
        income_population[i][j]=int(income_population[i][j])*6/14
        j+=1
    i+=1

#this is used to give an estimate on the population in the secondary education age
#https://data.unicef.org/topic/education/secondary-education/#:~:text=Though%20the%20duration%20in%20each,spanning%202%20to%203%20years). 
# Though the duration in each country vary, secondary education typically covers ages 12 to 17 and is divided into two levels: lower secondary education (spanning 3 to 4 years) and upper secondary education (spanning 2 to 3 years).
#therefore we estimate the population from 12 to 17 years old by calculating population(0-14)*6/14

def setKey(k):
    return k[1]

income_enrollment.sort(key=setKey)
income_population.sort(key=setKey)

#i=0
#while i<len(income_enrollment):
#    print(income_enrollment[i])
#    i+=1

enrollment=[]

i=0
while i<len(income_enrollment):
    l=[]
    l.append(income_enrollment[i][0])
    l.append(income_enrollment[i][1])
    l.append(income_enrollment[i][2])
    j=3
    while j<len(income_population[i]):
        l.append(int(float(income_enrollment[i][j])*int(income_population[i][j])/100))
        j+=1
    enrollment.append(l)
    i+=1

decade_enrollment=[]

i=0
while i<len(enrollment):
    l=[]
    l.append(enrollment[i][0])
    l.append(enrollment[i][1])
    #l.append(enrollment[i][2])
    j=0
    while j<5:
        sum=0
        k=j*10+3
        while k<j*10+13:
            sum+=enrollment[i][k]
            k+=1
        l.append(sum)
        j+=1
    decade_enrollment.append(l)
    i+=1

#print(decade_enrollment)

#enrollment contains information about the number of hgih schoolers by decades
#2-60, 3-70, 4-80, 5-90, 6-00, 7-10 index-decades

#We have processed all needed data set, then we need to start visualizeing them

#student_per_dot=int(input("please type the number of students per dot"))
student_per_dot=3000000

decade_enrollment_1=[]

i=0
while i<len(decade_enrollment):
    decade_enrollment_1.append(decade_enrollment[i])
    i+=1

decade_enrollment[0]=decade_enrollment_1[0]
decade_enrollment[1]=decade_enrollment_1[4]
decade_enrollment[2]=decade_enrollment_1[3]
decade_enrollment[3]=decade_enrollment_1[2]
decade_enrollment[4]=decade_enrollment_1[1]
#High income-0, Upper middle income-1, Low income-2, Lower middle income-3, middle income-4 (changed)
#print('\n',decade_enrollment)

decade_dot=[]

i=0
while i<len(decade_enrollment):
    l=[]
    l.append(decade_enrollment[i][0])
    l.append(decade_enrollment[i][1])
    if i==0:
        l.append("tomato") #color index
    if i==1:
        l.append("orange")
    if i==4:
        l.append("forestgreen")
    if i==2:
        l.append("mediumpurple")
    if i==3:
        l.append("deepskyblue")
    j=2
    while j<len(decade_enrollment[i]):
        l.append(int(int(decade_enrollment[i][j])/student_per_dot) )
        j+=1
    decade_dot.append(l)
    i+=1

#print(decade_dot)

#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from random import seed
from random import gauss
from random import random
import math

# Fixing random state for reproducibility
#np.random.seed(19680801)

def mod(k,r):
    return k-int(k/r)*r

#this defined a modulo function on real numbers. Convinient for polar coordinate

#print(mod(350.17,-23.49)) this is a test on the mod function

#radius_norm=int(input("please type in radius norm."))
radius_angle=[]
center_angle=[]
margin=5000
tot_angle=60
#radius angle is used to keep track of the curent radius of the tree at the current angle
dot_angle=[]
dot_radius=[]
dot_color=[]
dot_area=[]

j=3
while j<len(decade_dot[0]):
    l=[]
    i=0
    sum=0
    while i<len(decade_dot):
        sum+=decade_dot[i][j]
        i+=1
    l.append(0)
    i=1
    sum_2=0
    while i<len(decade_dot):
        sum_2+=360*decade_dot[i][j]/sum
        l.append(sum_2)
        i+=1
    center_angle.append(l)
    j+=1

#print(center_angle)

i=0
while i<tot_angle:
    radius_angle.append(1)
    i+=1

def random_angle(mean, std_dev):
    return gauss(mean,std_dev)

#def random_angle(mean, std_dev):
#    return mod(random()*360,71)+mean

def random_radius(r):
    #return math.sqrt(20/r)
    #return 20/r
    return 150*pow(r,1/15)

j=int(3)
while j<8:
    i=int(0)
    while i<len(decade_dot):
        p=0
        while p<decade_dot[i][j]:
            angle=mod(random_angle(center_angle[j-3][i],60),360)
            #print(angle,'\n')
            radius=random_radius(radius_angle[int(angle*tot_angle/360)])
            dot_angle.append(np.deg2rad(angle)) # to be continued
            dot_radius.append(radius+radius_angle[int(angle*tot_angle/360)])
            radius_angle[int(angle*tot_angle/360)]+=radius
            dot_color.append(decade_dot[i][2])
            dot_area=2
            p+=1
        i+=1
    k=0
    while k<tot_angle:
        radius_angle[k]+=margin 
        k+=1
    j+=1

ax = plt.subplot(projection='polar')
c = ax.scatter(dot_angle, dot_radius, c=dot_color, s=dot_area, alpha=0.5)
ax.grid(False)
plt.title("Representing Students Receiving Secondary Education As A Tree", fontdict = {'color':'forestgreen','size':16})
tomato_patch = mpatches.Patch(color='tomato', label='Upper Income')
orange_patch = mpatches.Patch(color='orange', label='Upper Middle Income')
mediumpurple_patch= mpatches.Patch(color='mediumpurple', label='Middle Income')
deepskyblue_patch= mpatches.Patch(color='deepskyblue', label='Lower Middle Income')
forestgreen_patch= mpatches.Patch(color='forestgreen', label='Low Income')
ax.legend(handles=[tomato_patch, orange_patch, mediumpurple_patch, deepskyblue_patch, forestgreen_patch])
plt.axis('off')
plt.show()
