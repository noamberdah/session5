# you have 3 lives. I roll the dice. If I roll 6, you win
# If not 6, you lose 1 life.

from random import randint

lives = 3
while lives > 0:
    roll = randint (a:1, b:6) #make sure to not put a: and b:!!
    if roll ==6:
        print("You rolled a 6! You win!")
        break # this exists the while even if lives still >0
    else:
        print(f"You rolled a {roll}! You lose a life")
        lives -= 1
        print(f"Lives left= {lives}")
else: # else from while !!