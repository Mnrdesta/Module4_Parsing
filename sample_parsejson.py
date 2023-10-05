import json

#Example json
x = '{"name":"Maenard", "age":"23", "city":"Antipolo"}'

#Parse json
y = json.loads(x)
print("The output of the json file is", y)
print("Name:", y["name"])
print("Age:", y["age"])
print("City:", y["city"])