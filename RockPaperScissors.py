# A simple game of rock paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:

    n = random.randint(0,2)
    print("Let's Play Rock Paper Scisorrs")
    choice = input("0 = Rock, 1 = Scissors , 2 = Paper\n")
    
    if int(choice) < 3:  
    
        choiceMap = [rock,scissors,paper]
        print("You chose " + choiceMap[int(choice)])
        print(" ")
        print("The computer chose " +choiceMap[n])
        print(" ")


        if n == int(choice):
                    print("There is a tie try again")
                    print(" ")
            
        elif (n==0) and (int(choice) == 2): # Rock Vs Paper
                        print("You Win!")
        elif (n == 1) and (int(choice) == 0): #Scissors VS Rock
                      print("You win")
        elif (n == 2) and (int(choice) == 1): #Paper Vs Scissors
                      print("You win")
                      print(" ")
        else: 
                  print("You Lose")
                  print(" ")

	  
    else:
        print(" ")
        print("Please input a number between 0 - 2")




