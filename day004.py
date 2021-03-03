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


player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computer = random.randint(0,2)

if player == 0:
  pchoice = rock
elif player == 1:
  pchoice = paper
else:
  pchoice = scissors
if computer == 0:
  cchoice = rock
elif computer == 1:
  cchoice = paper
else:
  cchoice = scissors  
print ("\nPlayer chose:")
print (pchoice)
print ("Computer chose:")
print (cchoice)
if player == 0:
  if computer == 0:
    print ("It's a draw")
  elif computer == 1:
    print ("You lose")
  else:
    print ("You win")
elif player == 1:
  if computer == 0:
    print("You win")
  elif computer == 1:
    print("Its a draw")
  else:
    print("You lose")
else:
  if computer == 0:
    print("You lose")
  elif computer == 1:
    print("You win") 
  else:
    print("It's a draw")