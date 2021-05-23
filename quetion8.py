a=["name","disignation","age","salery"]
b=["neelam","programer","24","2400",]
f={}
dict={}
dict1={}
dict2={}
dict3={}
for index in range(len(a)):
    dict[a[index]]=b[index]
# print(dict)
f["employee1"]=dict

a=["name","disignation","age","salery"]
c=["komal","trainer","24","20000"]
for index in range(len(a)):
    dict1[a[index]]=c[index]
# print(dict1)
f["employee2"]=dict1
a=["name","disignation","age","salery"]
d=["anuradha","HR","25","40000"]
for index in range(len(a)):
    dict2[a[index]]=d[index]
# print(dict2)
f["employee3"]=dict2
a=["name","disignation","age","salery"]
e=["Abhishek","manager","29","63000"] 
for index in range(len(a)):
    dict3[a[index]]=e[index]
# print(dict3) 
f["employee4"]=dict3
# print(f)
import json
with open("sample8.json","w") as outfile:
    json.dump(f,outfile,indent=10)


