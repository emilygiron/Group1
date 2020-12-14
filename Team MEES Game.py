# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:29:07 2020

@author: Emily Giron
"""
#this functions checks if the user has entered only 3 numbers
def check_num(number):
    while(number < 100 or number > 1000):
        print("\nYou did not enter a 3 digit number, please enter a 3 digit number")
        number = int(input("Guess the number: "))
    return number


import random 

while True:
    print("Welcome to the Mastermind game!")
    print("\nAll you have to do is to guess a three digit number in the least amount of tries!")
    
    num = random.randrange(100, 1000)   
      
    n = int(input("I'm thinking of a 3 digit number... Guess the number: ")) 
    check_num(n)
     
    
    #if player guess right on first try
    if (n == num):   
        print("Great! You guessed the number in just 1 try! You're a Mastermind!") 
    else: 
       #number of tries
        ctr = 0  
      
        # while loop repeats as long as the  
        # Player fails to guess the number correctly. 
        while (n != num):   
            ctr += 1  
            count = 0
      
            # explicit type conversion of an integer to 
            # a string in order to ease extraction of digits 
            n = str(n)   
      
            # explicit type conversion of a string to an integer 
            num = str(num)   
      
            # correct[] list stores digits which are correct 
            correct = ['X']*3
      
             
            for i in range(0, 3):  
      
                 # checking for equality of digits 
                if (n[i] == num[i]):   
                    # number of digits guessed correctly increments 
                    count += 1  
                    # hence, the digit is stored in correct[]. 
                    correct[i] = n[i]   
                else: 
                    continue
      
            # when not all the digits are guessed correctly. 
            if (count < 3) and (count != 0):   
                print("Not quite the number. But you did get ", count, " digit(s) correct!") 
                print("Also these numbers in your input were correct.") 
                for k in correct: 
                    print(k, end=' ') 
                print('\n') 
                print('\n') 
                n = int(input("Enter your next choice of numbers: ")) 
                n = check_num(n)
                
            # when none of the digits are guessed correctly. 
            elif (count == 0):   
                print("None of the numbers in your input match.") 
                n = int(input("Enter your next choice of numbers: "))
                n = check_num(n)
      
        # condition for equality. 
        if n == num:   
            print("You've become a Mastermind!") 
            print("It took you only", ctr, "tries.")
            
            #when the user guessed the right number, ask to play again
            play_again = input("Do you want to play again? (y/n): ")
            while play_again not in ["y", "n", "Y", "N"]:
                print(play_again)
                play_again = input("Please enter y to continue or n to quit: ")
            if play_again == "n" or play_again == "N":
                print("Thanks for playing!")
                break
