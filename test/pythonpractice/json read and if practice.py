import json
json_file = open("pythonpractice\json practice.json", "r", encoding="utf-8")
person = json.load(json_file)
json_file.close()

if "Nathan" in person.values(): 
    print("hello")
print("end")