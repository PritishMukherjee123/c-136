import csv
data=[]
with open("dataset_2.csv","r") as ff:
    csvreader=csv.reader(ff)
    for i in csvreader :
        data.append(i)

headers=data[0]
Planet_data=data[1:]

for i in Planet_data:
    i[2]=i[2].lower()

Planet_data.sort(key=lambda Planet_data:Planet_data[2])
with open("d2.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(Planet_data)
