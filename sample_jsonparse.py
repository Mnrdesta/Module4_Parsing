import json
with open('sample.json','r') as json_file:
    json_data = json.load(json_file)
    print(json_data)
    print(json.dumps(json_data,indent=4))

    Name = []
    for cert in json_data['certifications']:
            Name.append(cert['name'])

    print("Names:", Name)