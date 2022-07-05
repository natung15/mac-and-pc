secret_number = int(9)
Guess_count = 0
guess_limit = 3

while Guess_count < guess_limit:
    guess = int(input("Guess a number 1-9:"))
    Guess_count += 1
    if guess == secret_number:
        print("YOU WIN!")
        break
else:
    print("you lost! :(")
    

