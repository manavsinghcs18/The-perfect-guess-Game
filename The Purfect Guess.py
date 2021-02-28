import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0
while (userGuess != randNumber):
    userGuess=int(input("Enter your guess: "))
    guesses+=1
    if userGuess==randNumber:
        print("You guessed it Right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
print(f"Your gussed number in {guesses} guesses")
with open ("hiscore.txt","r") as f:
    hiscore=int(f.read())
if(guesses<hiscore):
    print("YOu have just broken the highscore!")
with open ("hiscore.txt","w") as f:
    f.write(str(guesses))
