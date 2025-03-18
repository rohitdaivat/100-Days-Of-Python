# Day 2 Project: Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_tip = bill * (tip / 100)
total = (bill + total_tip) / people
final_amount = round(total, 2)
print(f"Each person should pay: ${final_amount}")
