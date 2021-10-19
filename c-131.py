import csv
rows=[]

with open("planetdata.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers=rows[0]
Planet_data_row=rows[1:]
print(headers)
print(Planet_data_row[0])

headers[0]="row_num"
Solar_System_Planet_Count={}
for Planet_data in Planet_data_row:
    if Solar_System_Planet_Count.get(Planet_data[11]):
        Solar_System_Planet_Count[Planet_data[11]]+=1
    else:
        Solar_System_Planet_Count[Planet_data[11]]=1

max_solar_system=max( Solar_System_Planet_Count,key=Solar_System_Planet_Count.get)
print(max_solar_system)

temp_planet_data_rows= list(Planet_data_row)
for i in temp_planet_data_rows :
    planet_mass=i[3]
    if planet_mass.lower()=="unknown":
        Planet_data_row.remove(i)
        continue
    else :
        planet_mass_value=planet_mass.split(" ")[0]
        planet_mass_ref=planet_mass.split(" ")[1]
        if planet_mass_ref =="Jupiters":
            planet_mass_value= float(planet_mass_value)*317.8
        i[3]=planet_mass_value

    planet_radius=i[7]
    if planet_radius.lower()=="unknown":
        Planet_data_row.remove(i)
        continue
    else :
        planet_radius_value=planet_radius.split(" ")[0]
        planet_radius_ref=planet_radius.split(" ")[1]
        if planet_radius_ref =="Jupiter":
            planet_radius_value= float(planet_radius_value)*11.2
        i[7]=planet_radius_value

print(len(Planet_data_row))
koi_planets=[]
for i in Planet_data_row :
    if max_solar_system == i[11]:
        koi_planets.append(i)
print(len(koi_planets))

import plotly.express as px 
koi_planet_mass=[]
koi_planet_name=[]
for i in koi_planets :
    koi_planet_mass.append(i[3])
    koi_planet_name.append(i[1])

koi_planet_mass.append(1)
koi_planet_name.append("earth")
graph = px.bar(x=koi_planet_name,y=koi_planet_mass)
graph.show()

temp_planet_data_rows=list(Planet_data_row)
for i in temp_planet_data_rows:
    if i[1].lower()=="hd 100546 b":
        Planet_data_row.remove(i)

planet_mass =[]
planet_radius=[]
planet_name=[]
for i in Planet_data_row:
    planet_mass.append(i[3])
    planet_radius.append(i[7])
    planet_name.append(i[1])

planet_gravity=[]
for index , name in enumerate(planet_name):
    gravity=float(planet_mass[index])*5.972e+24/(float(planet_radius[index])*float(planet_radius[index])*6371000*6371000)
    gravity=gravity*6.674e-11
    planet_gravity.append(gravity)

graph=px.scatter(x=planet_radius,y=planet_mass,size=planet_gravity,hover_data=[planet_name])
graph.show()

low_gravity=[]
for index,gravity in enumerate(planet_gravity):
    if gravity<10 :
        low_gravity.append(Planet_data_row[index])

low_gravityplanets=[]
for index,gravity in enumerate(planet_gravity):
    if gravity<100 :
        low_gravityplanets.append(Planet_data_row[index])

print(len(low_gravity))
print(len(low_gravityplanets))

planet_type_values=[]
for i in Planet_data_row:
    planet_type_values.append(i[6])

print(list(set(planet_type_values)))

planet_masses=[]
planet_radiuses=[]
for i in Planet_data_row:
    planet_masses.append(i[3])
    planet_radiuses.append(i[7])

graph3=px.scatter(x=planet_radiuses,y=planet_masses)
graph3.show()

"""from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import seaborn as sb

X=[]
for  index,planet_mass in enumerate(planet_masses):
    temp_list=[planet_radiuses[index],planet_mass]
    X.append(temp_list)

Wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=42)
    kmeans.fit(X)
    Wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sb.lineplot(range(1,11),Wcss,marker="o",color="red")
plt.show()"""
planet_masses=[]
planet_radiuses=[]
planet_types=[]
for i in low_gravityplanets:
    planet_masses.append(i[3])
    planet_radiuses.append(i[7])
    planet_types.append(i[6])

graph4=px.scatter(x=planet_radiuses,y=planet_masses,color=planet_types)
graph4.show()

suitable_planets=[]
for i in low_gravityplanets : 
    if i[6].lower()=="terrestrial" or i[6].lower()=="super earth":
        suitable_planets.append(i)

print(len(suitable_planets))

temp_suitable_planets=list(suitable_planets)
for i in temp_suitable_planets :
    if i [8].lower()=="unknown":
        suitable_planets.remove(i)



for i in suitable_planets:
    if i[9].split(" ")[1].lower()=="days":
        i[9]=float(i[9].split(" ")[0])
    else:
        i[9]=float(i[9].split(" ")[0])*365
    i[8]=float(i[8].split(" ")[0])

orbital_radius=[]
orbital_period=[]
for i in suitable_planets:
    orbital_radius.append(i[8])
    orbital_period.append(i[9])

graph5=px.scatter(x=orbital_radius,y=orbital_period)
graph5.show()

goldilock_planet= list(suitable_planets)
temp_goldilock_planet=list(suitable_planets)
for i in temp_goldilock_planet:
    if float(i[8])<0.38 or float(i[8])>2 :
        goldilock_planet.remove(i)

print(len(goldilock_planet))
print(len(suitable_planets))

planet_speed=[]
for i in suitable_planets:
    distance = 2*3.14*i [8]*1.496e+9
    time =i[9]*86400
    speed=distance/time
    planet_speed.append(speed)

speed_suporting_planets=list(suitable_planets)
temp_speedsupporting=list(suitable_planets)
for index,pd in enumerate(temp_speedsupporting):
    if planet_speed[index]>200:
        speed_suporting_planets.remove(pd)

print(len(speed_suporting_planets))
print(len(suitable_planets))

habitableplanets=[]
for i in speed_suporting_planets:
    if i in temp_goldilock_planet :
        habitableplanets.append(i)

print(len(habitableplanets))

finaldict ={}
for index,planet_data in enumerate(Planet_data_row):
    feautureslist=[]
    gravity=(float(planet_data[3])*5.972e+24)/(float(planet_data[7])*float(planet_data[7])*6371000*6371000)*6.674e-11
    try:
        if gravity<100:
            feautureslist.append("gravity")
    except:pass
    try:
        if planet_data[6].lower()=="terrestrial" or planet_data[6].lower()=="super earth":
            feautureslist.append("planet_type")
    except:pass
    try:
        if planet_data[8] > 0.38 or planet_data[8]<2 :
            feautureslist.append("goldilock")
    except:pass
    try:
        distance=2*3.14*(planet_data[8]*1.496e+9)
        time=planet_data[9]*86400
        speed=distance/time
        if speed<200:
            feautureslist.append("speed")
    except:pass
    finaldict[index]=feautureslist

print(finaldict)
# graph.plot

gravity_planet_count=0
for key , value in finaldict.items():
    if "gravity" in value:
        gravity_planet_count+=1

print(gravity_planet_count)

type_planet_count=0
for key , value in finaldict.items():
    if "planet_type" in value:
        type_planet_count+=1

print(type_planet_count)



speed_planet_count=0
for key , value in finaldict.items():
    if "speed" in value :
        speed_planet_count+=1

print(speed_planet_count)

goldilock_planet_count=0
for key , value in finaldict.items():
    if"goldilock" in value :
        goldilock_planet_count+=1

print(goldilock_planet_count)

planet_not_gravity_support=[]
for i in Planet_data_row :
    if i not in low_gravityplanets :
        planet_not_gravity_support.append(i)

type_no_gravity_planet_count=0
for i in planet_not_gravity_support:
    if i[6].lower()=="terrestrial" or i[6].lower()=="super earth":
        type_no_gravity_planet_count+=1

print(len(planet_not_gravity_support))
print(type_no_gravity_planet_count)

final_dict1={}
for i,pd in enumerate(Planet_data_row):
    feautures_list =[]
    gravity=(float(pd[3])*5.972e+24)/(float(pd[7])*float(pd[7])*6371000*6371000)*6.674e-11
    try:
        if gravity<100 :
            feautures_list.append("gravity")
    except:
        pass
    try:
        if pd[6].lower()=="terrestrial" or pd[6].lower()=="super earth":
            features_list.append("planet_type")
    except:
        pass
    try:
        if pd[8]>0.38 or pd[8]<2 :
            features_list.append("goldilock")
    except:
        pass
    try:
        distance=2*3.14*(pd[8]*1.496e+9)
        time=pd[9]*86400
        speed=distance/time
        if speed<200 :
            features_list.append("speed")
    except:
        pass
    final_dict1[i]=feautures_list

print(final_dict1)