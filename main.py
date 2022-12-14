import numpy as np
import csv
from math import sqrt
import random

a=np.zeros((130,2),dtype=list)
l=np.zeros((130,2),dtype=list)
list=np.zeros((130,8),dtype=list)
dataSet1=[]
dataSet2=[]
q1=int(input("Ortam şıklığı puan 1-10"))
q2=int(input("Ortam temizliği puan 1-10"))
q3=int(input("Yemek kalitesi puan 1-10"))
q4=int(input("Hizmet kalitesi puan 1-10"))
q5=int(input("Fiyat uygunluğu puan 1-10"))
q6=int(input("Ulaşım kolaylığı puan 1-10"))
q7=int(input("Araç park olanağı puan 1-10"))
q8=0
bool=True
while(bool == True):
    q8 = int(input("Kac adet restoran gosterilsin 1-15"))
    if 0<q8<16 :
        bool=False





dataSet1.append(q1)
dataSet1.append(q2)
dataSet1.append(q3)
dataSet1.append(q4)
dataSet1.append(q5)
dataSet1.append(q6)
dataSet1.append(q7)

def cosine_similarity(dataSet1,dataSet2):
    sum1=0
    sum2=0
    sum3=0
    for i in range(0,len(dataSet1)):
        sum1 = sum1 + (dataSet1[i] * dataSet1[i])
        sum2 = sum2 + (dataSet2[i] * dataSet2[i])
        sum3 = sum3 + (dataSet1[i] * dataSet2[i])
    sum1 = sqrt(sum1)
    sum2 = sqrt(sum2)

    return sum3 / (sum2 * sum1)

def sorting(dataSet):
    return 10

def pearson_correlation(dataSet1,dataSet2):
    result=0
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    a=len(dataSet1)
    for i in range(0,a):
        sum1 = sum1 + dataSet1[i]
        sum2 = sum2 + dataSet2[i]
        sum3 = sum3 + dataSet1[i] * dataSet1[i]
        sum4 = sum4 + dataSet2[i] * dataSet2[i]
        sum5 = sum5 + dataSet1[i] * dataSet2[i]


    b = (a * sum5 - (sum1 * sum2)) / sqrt(((a * sum3 - (sum1 * sum1)) * (a * sum4 - (sum2 * sum2))))
    return b

filename='restoran-oneri.txt'
line_count=0
with open(filename, 'r') as csvfile: #islemler yapabilmek icin matrise cevirdim.

    csvreader = csv.reader(csvfile)

    for row in csvreader:

        for i in range(0, 8):
            list[line_count - 1][i] = row[i]
        line_count += 1

for i in range(0,130):
    for j in range(0,8):
        if (list[i][j] == "?"):
            list[i][j] = random.randint(1, 10)


for i in range(0,130):
    dataSet2.clear()
    for j in range(1,8):
        dataSet2.append(int(list[i][j]))
    cos=cosine_similarity(dataSet1,dataSet2)
    l[i][0] = list[i][0]
    l[i][1] = cos
    per=pearson_correlation(dataSet1,dataSet2)
    a[i][0] = list[i][0]
    a[i][1] = abs(per) #tum degerlerin mutlak degerini aldim cunku -1 ile 1 korelasyon esittir.

for i in range(0,130):
    for j in range(i+1,130):
        if l[i][1]<l[j][1]:
            temp1=l[i][1]
            temp2=l[i][0]
            l[i][1]=l[j][1]
            l[i][0]=l[j][0]
            l[j][1]=temp1
            l[j][0]=temp2

for i in range(0,130):
    for j in range(i+1,130):
        if a[i][1]<a[j][1]:
            temp1=a[i][1]
            temp2=a[i][0]
            a[i][1]=a[j][1]
            a[i][0]=a[j][0]
            a[j][1]=temp1
            a[j][0]=temp2


for i in range(0,q8):
    print(l[i][0],l[i][1],a[i][0],a[i][1])