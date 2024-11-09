import random #first thing we need to import random to generate the random number we need
#generating a random number between 0 and 100
game_number = random.randrange(0,100)
 #user_input need to specify a number in an input
while(True):    
    try:  
        user_input =  int(input('guess the number ! '))
        if(user_input > game_number):        
                print('too high')       
        elif(user_input < game_number):
                print('too low')            
        else:
                print('you guessed right!')
                break
    except ValueError:
        print('enter a valid number please')
        

