def car_game():  
    carstatus = 0
    print("start - to start the car")
    print('stop - to stop the car')
    print('quit - to exit')
    while True:
        
        msg = input("> ").lower()
        if msg == "help":
            print("start - to start the car")
            print('stop - to stop the car')
            print('quit - to exit')
        elif msg == "start":
            if carstatus == 1:
                print('Car is already started')
            elif carstatus == 0:
                print("Car started ready to go!")
                carstatus += 1
        elif msg == 'stop':
            if carstatus == 1:
                print('Car has stopped.')
                carstatus -= 1
            elif carstatus == 0:
                print("Car is already stopped")
        elif msg == 'quit':
            break
        else:
            print("I don't understand that..")

