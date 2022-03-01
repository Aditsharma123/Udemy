# f-string
"""
var = 9.012
tree = 8.9303243

print(f"Your var is {var,tree}")
"""

yearOne = 365  # Days
yearTwo = 52  # weeks
yearThree = 12  # months

age = int(input("Enter your current age: "))
Living_Days = round((age * yearOne))
Living_Weeks = round((age * yearTwo))
Living_Months = round((age * yearThree))
Living_Years = round(90-age)

print(f"Your days left: {Living_Days} , Your months left: {Living_Months} , Your years left: {Living_Years}")
print(f"Your Weeks left: {Living_Weeks}")

