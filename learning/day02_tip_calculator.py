print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
individual_pay=(bill/people)
tip_percent = tip/100
total_pay=individual_pay* (1+tip_percent)
print(f"Each person should pay: ${total_pay:.2f}")

