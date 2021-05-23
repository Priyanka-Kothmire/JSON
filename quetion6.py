import json
a = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(a)
b = json.loads(a)
print("\nUnique Key in a JSON object:")
print(b)








