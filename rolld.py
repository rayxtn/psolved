import random 

while(True):
    choice = input("Wanna play a game? ").lower()
    if choice == 'y':
        dice_roll1 = random.randrange(1,6)
        dice_roll2 = random.randrange(1,6)
        print('Value of dice is' ,{dice_roll1},{dice_roll2})
    elif choice == 'n':
        print('thanks for playing !')
        break
    else:
        print('invalid choice!')        

