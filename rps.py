import random

my_list = ["rock", "paper" , "scissor"]
# program should choose something from the list
my_choice = random.choice(my_list)
# user should input his choice
while(True):
    try:
        user_choice = input('rock paper or scissor ? type R,P or S ')
    except ValueError:
        print('wrong choice !')
        if(user_choice not in my_list):
            print('you should choose R P or S')
            break
    continue_choice = input('wanna continue? Y,N?')        
    if ( continue_choice == 'n'.upper() or continue_choice == 'no'.upper() ):
     break        


 
       