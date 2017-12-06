import random
print("Let's play rock, paper scissors!")
p1= input('Enter one of the following: "rock", "paper", or "scissors": ')
while(p1 != "rock" and p1!= "paper" and p1!= "scissors"):
  p1= input('Enter one of the following: "rock", "paper", or "scissors": ')
p2= random.randint(1,3)

if (p2 == 1):
  p2 = "rock"
if (p2 == 2):
  p2 = "paper"
if (p2 == 3):
  p2 = "scissors"
  
if (p1 == "rock"):
  if (p2 == "scissors"):
    print("The other player chose scissors. You win!")
  if (p2 == "paper"):
    print("The other player chose paper. You lose!")
  if(p2 == "rock"):
    print("The other player chose rock. It's a draw!")

if (p1 == "paper"):
  if (p2 == "scissors"):
    print("The other player chose scissors. You lose!")
  if (p2 == "rock"):
    print("The other player chose rock. You win!")
  if (p2 == "paper"):
    print("The other player chose paper. It's a draw!")

if (p1 == "scissors"):
  if (p2 == "rock"):
    print("The other player chose rock. You lose!")
  if (p2 == "paper"):
    print("The other player chose paper. You win!")
  if (p2 == "scissors"):
    print("The other player chose scissors. It's a draw!")
