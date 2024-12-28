import random, sys, time

answer = random.randint(1,100)
guessCount = 0
print ('I am thinking of a number 1 - 100, can you guess it?')
while True:
    userGuess = int(input())
    if userGuess < answer:
        print('Too Low, Guess again!')
        guessCount = guessCount + 1 
        continue
    elif userGuess == answer:
        print('You got it! In ' + str(guessCount + 1) + ' tries!')
        sys.exit
    elif userGuess > answer:
        print('Too High, Guess again!')
        guessCount = guessCount + 1 
        continue 
 