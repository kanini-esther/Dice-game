import random
import time

roll_again = "yes"

while roll_again == "yes" or roll_again =="y" or roll_again == "Yes" or roll-again == "Y":
    print("\nRollng the dice...")
    time.sleep(1)

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The values are:")
    print("you rolled a double")

    if dice1 == dice2:
        print("you rolled a double")
    else:
        print("keep trying")
    roo_again = input("\nRoll the dice again? (y/n) ")
    
