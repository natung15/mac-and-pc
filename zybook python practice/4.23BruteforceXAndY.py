from re import I


Value1 = int(input("Value1:"))
Value2 = int(input("Value2:"))
Value3 = int(input("Value3:"))
Value4 = int(input("Value4:"))
Value5 = int(input("Value5:"))
Value6 = int(input("Value6:"))

for i in range(-10,10,1):
    for j in range(-10,10,1):
        xtest1 = Value1 * i
        ytest1 = Value2 * j
        xtest2 = Value4 * i
        ytest2 = Value5 * j
        if xtest1 + ytest1 == Value3 and xtest2 + ytest2 == Value6:
            print(f"x = {xtest1}, y = {ytest1}") 
            

