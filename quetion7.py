import json
  
  
# the file to be converted to 
# json format
filename = "JSON/Text.txt"
  
# dictionary where the lines from
# text will be stored
dict1 = {}
  
# # creating dictionary
with open(filename) as fh:
  
    for line in fh:
  
# #         reads each line and trims of extra the spaces 
# #         and gives only the valid words
        command, description = line.strip().split(None, 1)
  
        dict1[command] = description.strip()
        
# print(dict1)
  
# with open ("swati.json","w") as fh:
#     json.dump(dict1,fh,indent=4)
# fh.close()
# creating json file
# the JSON file is named as test1
out_file = open("sample7.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()

# # # a_dictionary = {}

# a_file = open("Text.txt")

# for line in a_file:

#     # key, value = line.split()

# # Split line into a tuple


#     a_dictionary[key] = value

# # Add tuple values to dictionary

# print(a_dictionary)

# dictionary = {}
# with open("Text.txt", "r") as file:
#     for line in file: 
#         key, value = line.strip().split(",")
#         dictionary[key] = value
# print(dictionary)
# import json
# with open("Text.txt") as fh:
#      commands = dict(line.strip().split(None, 1) for line in fh)
# print(json.dumps(commands, indent=2, sort_keys=True))




# import json

# filename = 'Text.txt'

# commands = {}
# with open("Text.txt","r") as fh:
#     for line in fh:
#         command, description = line.strip().split(' ', 1)
#         commands[command] = description.strip()

# print(json.dumps(commands, indent=2, sort_keys=True))


# import json

# filename = 'Text.txt'

# commands = {}
# with open("piyu.json) as fh:
#     for line in fh:
#         command, description = line.strip().split(' ', 1)
#         commands[command] = description.strip()

# print(json.dumps(commands, indent=2, sort_keys=True))


# f = open("Text.txt", 'r')
# answer = {}
# for line in f:
#     k, v = line.strip().split('=')
#     answer[k.strip()] = v.strip()

# f.close()


# d = {}
# with open("Text.txt") as f:
#     for line in f:
#         (key, val) = line.split()
#         d[int(key)] = val

#     print (d)

# filename = 'Text.txt'

# commands = {}
# with open(filename) as fh:
#     for line in fh:
#         command, description = line.strip().split(' ', 1)
#         commands[command] = description.strip()

# print(json.dumps(commands, indent=2, sort_keys=True))

