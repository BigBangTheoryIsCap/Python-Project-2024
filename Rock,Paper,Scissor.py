import random
import sys

# Initialize counters outside the loop
winCount = 0
loseCount = 0
tieCount = 0

while True:
    rChoice = random.randint(1, 3)
    print('What do you pick? (r)ock, (p)aper, (s)cissors, or (q)uit')
    pChoice = input().lower().strip()  # Ensure input is lowercase and stripped of extra spaces

    if pChoice == 'q':  # Check for quit input
        print(str(winCount) + ' wins, ' + str(loseCount) + ' losses, and ' + str(tieCount) + ' ties.')
        sys.exit()  # Exit the program immediately

    # Validate player input
    if pChoice not in ['r', 'p', 's']:
        print("Invalid choice. Please choose 'r', 'p', 's', or 'q'.")
        continue

    # Map random choices to names for cleaner code
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    print('Computer chose ' + choices[rChoice] + '.')

    # Determine outcome
    if (rChoice == 1 and pChoice == 'r') or \
       (rChoice == 2 and pChoice == 'p') or \
       (rChoice == 3 and pChoice == 's'):
        print("Hmm, it's a Tie. But not for long, I will WIN!")
        tieCount += 1
    elif (rChoice == 1 and pChoice == 'p') or \
         (rChoice == 2 and pChoice == 's') or \
         (rChoice == 3 and pChoice == 'r'):
        print("You might have won this one, but it's not going to stay that way!")
        winCount += 1
    else:
        print("HAHA, you LOSE! Better luck next time.")
        loseCount += 1
