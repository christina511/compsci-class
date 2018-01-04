#vending machine
monies = float(input("Enter an amount of monies. The vending machine will output the same amount in the least amount of coins: "))
quarters = monies//.25
monies = monies - (quarters*.25)
dimes = monies//.10
monies = monies - (dimes*.10)
nickels = monies//.05
monies = monies - (nickels*.05)
pennies = monies//.01
print("Quarters:" , quarters)
print("Dimes:", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)

#for some reason the extra penny won't work ._.
