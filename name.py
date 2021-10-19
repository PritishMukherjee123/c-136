import csv
dataset1=[]
dataset2=[]

with open("final.csv","r") as ff:
    csvreader=csv.reader(ff)
    for i in csvreader:
        dataset1.append(i)

with open("d2.csv","r") as ff:
    csvreader=csv.reader(ff)
    for i in csvreader:
        dataset2.append(i)

header1=dataset1[0]
header2=dataset2[0]
Planet_data1=dataset1[1:]
Planet_data2=dataset2[1:]

headers=header1+header2
Planet_data=[]

for index,data in enumerate(Planet_data1):
    Planet_data.append(Planet_data1[index]+Planet_data2[index])

with open("merge.csv","a+")as ff:
    csvwriter=csv.writer(ff)
    csvwriter.writerow(headers)
    csvwriter.writerows(Planet_data)

