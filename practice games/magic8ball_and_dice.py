from operator import truediv
from pdb import Restart
from pickle import FALSE
import random
from timeit import repeat

arcadestatus = True

class Games:
    def magicball():
        answers = ("yes", 'no', 'maybe', 'ask again', 'yes', 'no')
        answer = random.choice(answers)
        if answer != ('ask again'):
            input('Ask a Question to the magic 8 ball:')
            print(answer)
        else:
            while answer == ('ask again'):
                input('Ask a Question to the magic 8 ball:')
                print(answer)
                answer = random.choice(answers)
            while answer != ('ask again'):
                input('Ask a Question to the magic 8 ball:')
                print(answer)
                break
            
            

       
            
    def diceroll():
        x=1
        while x==1:
            try:
                dice = int(input("how many pairs of dice do you want to roll?:"))
                for i in range(dice):
                    rng1 = random.randint(1,6)
                    rng2 = random.randint(1,6)
                    print(f"({rng1},{rng2})")
                    x=0
            except ValueError:
                print("Please input a number!")



















"""print("Do you wanna play some games?")
x = 0
while x == 0:
    try:
        pick_game = int(input("Pick a game [1](Magic 8 ball) [2](Roll some dice) [3](Exit):"))
        if pick_game == 1:
                input('Ask a Question to the magic 8 ball:')
                answers = ("yes", 'no', 'maybe', 'ask again', 'yes', 'no')
                print(random.choice(answers))
                play_more = int(input("do you want to play more games? [1] Yes [2] No "))
                if play_more == 2:
                    print("Closing game...")
                    x =+ 1
        
        elif pick_game == 2:
            try:
                dice = int(input("how many pairs of dice do you want to roll?:"))
                for i in range(dice):
                    rng1 = random.randint(1,6)
                    rng2 = random.randint(1,6)
                    print(f"({rng1},{rng2})")
                play_more = int(input("do you want to play more games? [1] Yes [2] No "))
                if play_more == 2:
                    print("Closing game...")
                    x =+ 1
            except ValueError:
                print("please enter a number!")
        elif pick_game == 3:
            print("Closing game...")
            x =+ 1
    except ValueError:
        print("please insert a game number!")"""
