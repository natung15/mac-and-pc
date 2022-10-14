


height = int(input("Height:"))
width = int(input("Width:"))
arrowWidth = int(input("Arrow Width:"))


for x in range(height):
    for x in range(width):
        print("*",end="")
    print(" ")


if arrowWidth > width:
    for y in range(arrowWidth,0,-1):
        for x in range(y):
            print("*",end="")
        print("")

