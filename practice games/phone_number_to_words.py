def number_translator(): 
    phonenumber = input("Phone: ")
    number_key = {
        "1":"one ",
        "2":"two ",
        "3":"three ",
        "4":"four ",
        "5":"five ",
        "6":"six ",
        "7":"seven ",
        "8":"eight ",
        "9":"nine ",
        "0":"zero ",
        "-":""
    }
    output = ""
    for ch in phonenumber:
        output += number_key.get(ch,"!") + ""
    #for each character in the input "phonenumber"it is plugging in the key from each of the inputs and getting each value and adding a space
    print(output) 