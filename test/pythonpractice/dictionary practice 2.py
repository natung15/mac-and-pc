mydict = {"name": "Arif", "age": "18", "state": "Texas"}

mydict2 = dict(name="Nathan", age=30, state="Utah")

value = mydict2["name"]
print(value)

mydict["email"] = "arif@xyz.com"
print(mydict)

if "name" in mydict2:
    print(mydict2["name"])

for key, value in mydict.items():
    print(key, value)