import json
dict1={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
# out_file = open("piyu.json", "w")

# json.dump(dict1, out_file,sort_keys=True)

# out_file.close() 

with open("sample4.json","w") as f:
    json.dump(dict1,f,sort_keys=True)

    




