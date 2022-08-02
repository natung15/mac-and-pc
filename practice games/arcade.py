from operator import truediv
import magic8ball_and_dice
import phone_number_to_words
import secret_number_game
import car_game

arcadestatus = True
def playmore():
    global play_more
    play_more = int(input("do you want to play more games? [1] Yes [2] No "))
    
while arcadestatus == True:
    try:
        print('Pick a game "Magic 8ball", "Dice", "Car Game", "Number Translator", "Secret Number game", "Exit"')
        game_picker = input(">").lower()
        if game_picker == ("magic 8ball"):
            magic8ball_and_dice.Games.magicball()
            playmore()
            if play_more == 2:
                print("Closing game...")
                arcadestatus = False
        if game_picker == ('dice'):
            magic8ball_and_dice.Games.diceroll()
            playmore()
            if play_more == 2:
                print("Closing game...")
                arcadestatus = False
        if game_picker == ('number translator'):
            phone_number_to_words.number_translator()
            playmore()
            if play_more == 2:
                print("Closing game...")
                arcadestatus = False
        if game_picker == ('secret number game'):
            secret_number_game.guess_number()
            playmore()
            if play_more == 2:
                print("Closing game...")
                arcadestatus = False
        if game_picker == ('car game'):
            car_game.car_game()
            playmore()
            if play_more == 2:
                print("Closing game...")
                arcadestatus = False
        if game_picker == ('exit'):
            print("Closing game...")
            arcadestatus = False
       

        #if game_picker == (''):
        else:
            print("Please make sure the game is typed in correctly!")
    except ValueError:
        print("Please check your inputs!")
    
 


    

