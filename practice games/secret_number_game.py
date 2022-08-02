import random
secret_number = int(9)
Guess_count = 0
guess_limit = 3

'''while Guess_count < guess_limit:
    guess = int(input("Guess a number 1-9:"))
    Guess_count += 1
    if guess == secret_number:
        print("YOU WIN!")
        break
else:
    print("you lost! :(")'''
    
def guess_number():

            print("You have 3 tries to guess a number 1-10.") 
            print("On the final guess you get a hint.")
            secret_number = random.randint(1,10)
            Guess_count = 0
            guess_limit = 3
            global gorl
            if secret_number > 5:
                gorl = ("greater")
            if secret_number < 5:
                gorl = ("less")
           
            while Guess_count < guess_limit:
                try:
                    guess = int(input("Your guess:"))
                    if guess == secret_number:
                        print("YOU WIN!")
                        break
                    if guess != secret_number:
                        print("WRONG!")
                        Guess_count += 1
                    if Guess_count == 2:
                        print(f"The number is {gorl} than 5")
                except ValueError:
                    print("Please insert a valid number")
            if Guess_count == 3:
                print("You Lost :(")
                print(f"The secret number was {secret_number}")
                
      
   
        




