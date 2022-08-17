from base64 import encode
gamestatus = True
while gamestatus == True:
    answer = input("Hi there how are you? >").lower()
    if answer != ("bad"):
        print("I love you kyla :3")
        print("Come give me a hug")
        hug_or_not = input("Do you give him a hug? [Yes] or [No] >").lower()
        if hug_or_not == ("yes"):
            print('Nathan embraces you')
            print('Nathan says "I Love You"')
            print(":*")
            break
        if hug_or_not == ("no"):
            print("Nathan Dies")
            break
    if answer == ("bad"):
        print("Aweee poor baby come give me a hug and kiss :*")
        hug_kiss = input(":* or no >")
        if hug_kiss == (":*"):
            print(":**** I Love you now come here")
            break
        if hug_kiss == ("no"):
            print("OH NO NATHAN DIED")
            break