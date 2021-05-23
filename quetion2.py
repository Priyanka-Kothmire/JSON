import json
a={'name': "David",
     'class':"I",
     'age': 6  
    }
with open("sample2.json","w")as outfile:
    json.dump(a,outfile)
