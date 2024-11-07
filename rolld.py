import random 

play = ''
while(play == 'y'):
    play = input("Wanna play a game? ")
    x = random.randrange(0,6)
    y = random.randrange(0,6)
    print("Value of dice is: ",x," ",y)

print("Thanks for playing")    