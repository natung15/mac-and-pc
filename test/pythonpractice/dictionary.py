

c = {}
c["boys"] = {}
c["girls"] = {}
c = {"boys":{"george":True, "Tom":True,"annie":False, "mary":False}}
c = {"girls":{"george":False, "Tom":False,"annie":True, "mary":True}}

c = {"gays":{"kyla":True,"nathan":False}}

d = {}
d["george"] = {}
d["george"] = 24
d["tom"] = 32

e = {}
e["annie"] = 30
e["mary"] = 18


for key, value in c.items():
    print("key:")
    print(key)
    print("value")
    print(value)
