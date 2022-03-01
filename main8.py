from my import randomNumber


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

# Write your code below this line 👇

Choice = int(input("0 for Rock\n1 for paper\n2 for scissors\nEnter here: "))
if Choice == 0 and randomNumber == 0:
    print("Your choice: ", rock)
    print("computer's choice: ", rock)
    print("There is a draw")

elif Choice == 0 and randomNumber == 1:
    print("Your choice: ", rock)
    print("Computer's choice: ", paper)
    print("You lost")

elif Choice == 0 and randomNumber == 2:
    print("Your choice: ", rock)
    print("Computer's choice: ", scissors)
    print("You Won")

if Choice == 1 and randomNumber == 0:
    print("Your choice: ", paper)
    print("computer's choice: ", rock)
    print("You Won")

elif Choice == 1 and randomNumber == 1:
    print("Your choice: ", paper)
    print("Computer's choice: ", paper)
    print("There is a draw")

elif Choice == 1 and randomNumber == 2:
    print("Your choice: ", paper)
    print("Computer's choice: ", scissors)
    print("You Lost")

if Choice == 2 and randomNumber == 0:
    print("Your choice: ", scissors)
    print("computer's choice: ", rock)
    print("You lost")

elif Choice == 2 and randomNumber == 1:
    print("Your choice: ", scissors)
    print("Computer's choice: ", paper)
    print("You Won")

elif Choice == 2 and randomNumber == 2:
    print("Your choice: ", scissors)
    print("Computer's choice: ", scissors)
    print("There is a draw")
