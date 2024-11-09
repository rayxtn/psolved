import random #first thing we need to import random to generate the random number we need
#generating a random number between 0 and 100
game_number = random.randrange(0,100)
 #user need to specify a number in an input
user_input =  input('guess the number ! ')
user_inputInt = int(user_input)
while(user_inputInt != game_number): 
    if(user_inputInt > game_number):        
        print('too high')
        break
    elif(user_inputInt < game_number):
        print('too low')    
        break
    else:
        print('you guessed right!')
