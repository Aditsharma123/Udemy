print("Welcome to tip calculator")
totalBill = float(input("What was the total bill: "))
Percentage = float(input("What percentage would you like to give(10,20,30,40,50,60...)?: "))
People = int(input("How many people to split the bill?: "))

tip_as_percent = Percentage/100
total_tip_amount = totalBill * tip_as_percent
Answer = totalBill+total_tip_amount
lAnswer = Answer / People
finalAnswer = round(lAnswer, 2)

print(f"Every person should give: {finalAnswer}")
