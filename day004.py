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

import random
choices = ["rock", "paper", "scissors"]
print (f"Choices = {choices}")
pchoice = input("What do you choose: ")

#graphics
print(f"Player chooses {pchoice}")
if pchoice == "rock":
  print(rock)
elif pchoice == "paper":
  print(paper)
elif pchoice == "scissors":
  print(scissors)
else:
  print("Invalid selection")
  state = "lose"
cchoice = random.choice(choices)
print(f"Computer chooses {cchoice}")
if cchoice == "rock":
  print(rock)
elif cchoice == "paper":
  print(paper)
elif cchoice == "scissors":
  print(scissors)

#win/lose logic
if pchoice == "rock":
  if cchoice == "rock":
    state = "tie"
  elif cchoice == "scissors":
    state = "win"
  elif cchoice == "paper":
    state = "lose"

elif pchoice == "paper":
  if cchoice == "paper":
    state = "tie"
  elif cchoice == "rock":
    state = "win"
  elif cchoice == "scissors":
    state = "lose"

elif pchoice == "scissors":
  if cchoice == "scissors":
    state = "tie"
  elif cchoice == "paper":
    state = "win"
  elif cchoice == "rock":
    state = "lose"

print (f"You {state}!")

  
