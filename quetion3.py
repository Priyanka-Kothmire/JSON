import json
students={'name':"shivam",'class':"b.com",'rollno':50,}
# students=json.dumps(students)
# print(type(students))
# print(students)
with open("sample3.json","w")as f:
    json.dump(students,f)
