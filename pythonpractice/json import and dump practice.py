import json
json_file = open("pythonpractice\practice.json", "r", encoding="utf-8")
person = json.load(json_file)
json_file.close()

json.dumps(person)

print(person)

persontwo = {}
persontwo["name"] = "Kyla"
persontwo["age"] = "18"
persontwo["gender"] = "female"
persontwo["height"] = "5'1"
persontwo["birthday"] = "1/29/04"
file2 = open("pythonpractice\practice dump.json", "w", encoding="utf-8")
json.dump(persontwo ,file2)
file2.close

