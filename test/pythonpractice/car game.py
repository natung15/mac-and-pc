import random



def car_game():
    game_status = True
    car_gas = 10
    car_status = 0
    car_health = 10
    car_wheels = 4
    visibility = 8
    Cash = 100
    player_health = 10
    stats = 1
    print("Welcome to car game a pick your own adventure game")
    print("choose one of the options")
    print("Start - To start the game")
    print('Quit - to exit')
    start_quit = input(">").lower()
    if start_quit == ("quit"):
        game_status = False
    global event
    event = random.randint(1,2)

    
    while game_status == True:
        if car_gas == 0:
            print(f"|Gas-{car_gas}/10|")
            print("Game Over!")
            break
        if stats == 1:
            car_gas -= 1
            visibility = random.randint(0,8)
            print(" ")
            print(f"|Gas-{car_gas}/10|")
            print(f"|Car Condition-{car_health}/10|")
            print(f"|Visibility-{visibility}/8|")
            print(f"|Wheels-{car_wheels}/4|")
            print(f"|Cash-{Cash}$|")
            print(" ")
            stats -= 1
        if visibility == 0:
            print(f"|Visibility-{visibility}/8|")
            print("You are caught in a sandstorm")
            step_out = input("[Yes] or [No]").lower()
            if step_out == ("yes"):
                print("You Died")
                print("Game Over!")
                game_status = False
            


        if event == 1:
            stats = 1
            global gas_station
            print("you pass by a gas station do you drive in?")
            gas_station = input("[Yes] or [No] ").lower()
            if gas_station == ("yes"):
                event_gas_station = random.randint(1,4)
                if event_gas_station == (1):
                    print(" ")
                    print("|you found a 20$ on the ground|")
                    print(f"|Cash-{Cash}$|")
                    Cash += 20
                    event_gas_station = (2)
                if event_gas_station != (1):
                    gas_station_fill_up = 10 - car_gas 
                    gas_price = gas_station_fill_up * 5 
                    print(" ")
                    print(f"Do you want to fill up gas to full? ({gas_price}$)" )
                    print(f"|Gas-{car_gas}/10| ")
                    fill_up = input("[Yes] or [No] ").lower()
                    if fill_up == ("yes"):
                        Cash -= gas_price
                        for number in range(gas_station_fill_up):
                            car_gas +=1
                        car_gas +=1
                        event = random.randint(1,2)
                    if fill_up == ("no"):
                        event = random.randint(1,2)


        if event == 2:
            stats = 1
            print("You see a hitch hiker on the side of the road")
            print("Do you pick them up?")
            hitch_hiker_pick_up = input("[Yes] or [No] ").lower()
            if hitch_hiker_pick_up == ("yes"):
                which_hitch_hiker = random.randint(1,10)
                if which_hitch_hiker == 1:
                    print("The hitch hiker sits behind you and stabs you in the neck and takes your car")
                    print(" ")
                    print("You Died")
                    print("Game Over!")
                    game_status = False
                if which_hitch_hiker != 1:
                    good_deed = random.randint(1,3)
                    if good_deed == (1,2):
                        print("The hitch hiker gave you some cash for the trip and thanks you")
                        Cash += 30
                    if good_deed == 3:
                        print("The hitch hiker slashes one of your tires before he leaves")
                        car_wheels -= 1
                        car_health -= 2
            if hitch_hiker_pick_up == ("no"):
                print("You drove ")

            event == 0
            
        



   
                            

        
        
        
                






car_game()










#def car_game():  
'''carstatus = 0
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
            print("I don't understand that..")'''
