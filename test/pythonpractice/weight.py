from re import L
from sqlite3 import converters


weight = float(input("Weight: "))
lbs_or_kg = input("(K)g or (L)bs: ")

if lbs_or_kg.upper() == "L":
    converted = weight / 2.20462
    print('weight in kg: ' + str(converted))
else:
    converted = weight * .45
    print('weight in lbs: ' + str(converted))