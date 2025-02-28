# we need the random "library"
from random import randrange

#makes a number btwn 0-100 (excluding 100)
#saves it into a variable called "answer"
answer = randrange(100)

#runs the code inside of the while loop forever
while True:
    #ask the player for a number and save it
    player_guess = int(input("Guess a number: "))

    if (answer == player_guess):
        print("You win!") #print win message
        break #ends game by breaking the loop
    if (player_guess > answer):
        print("It's smaller.")
    else:
        print("It's bigger.")

#n = randrange(1000)
#while True:
    #v = int(input())
    #if n == v:
        #print('You win!')
        #break
    #print('Smaller' if (n<v) else 'Bigger')