import random
action = input('You encounter a monster with 100 health. You also start with 100 health. Do you choose to "run" or "hit" the monster?')
monstHealth = 100
playerHealth = 100
while (action == "hit" and monstHealth >0 and playerHealth > 0):
  monstDamage = random.randint(1,10)
  monstHealth = monstHealth - monstDamage
  playerDamage = random.randint(1,10)
  playerHealth = playerHealth - playerDamage
  print("You dealt", monstDamage, "points of damage to the monster.")
  print("The monster attacked you back, dealing", playerDamage, "points of damage to your life points." )
  if (monstHealth > 0):
    print("Monster's health:", monstHealth)  
  if (playerHealth > 0):
    print("Your health:", playerHealth)
  if (playerHealth >0 and monstHealth > 0):
    action = input('\nDo you choose to "run" or "hit" the monster?')
if (monstHealth <=0):
  print("\nYou have defeated the monster and claimed victory!!! :)")
elif (playerHealth<=0):
  print("Oh no! The monster defeated you. Better luck next time!")
if (action == "run"):
  print("\nRan away safely!")
