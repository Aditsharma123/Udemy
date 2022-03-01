print("Welcome to pizza deliveries")
size = input("What should be the size of pizza(s for small,m for medium,l for large): ")
print("Small pizza: $10")
print("Medium pizza: $20")
print("Large pizza: $25")

peperoni = input("Would you like to add peperoni(y,n)( +$2): ")
cheese = input("Would you like to add extra cheese(y,n)( +$3): ")

if size == "s" and peperoni == "y" and cheese == "y":
    print("You should pay($10 + $2 + $3):$15")
elif size == "m" and peperoni == "y" and cheese == "y":
    print("You should pay($20 + $2 + $3):$25")
elif size == "l" and peperoni == "y" and cheese == "y":
    print("You should pay($25 + $2 + $3):$30")

# =-=-=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=

if size == "s" and peperoni == "n" and   cheese == "y":
    print("You should pay($10 + $3):$13")
elif size == "m"  and   peperoni == "n" and   cheese == "y":
    print("You should pay($20 + $3):$23")
elif size == "l"  and   peperoni == "n" and   cheese == "y":
    print("You should pay($25 + $3):$28")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

if size == "s" and  peperoni == "y" and   cheese == "n":
    print("You should pay($10 + $2):$12")
elif size == "m"  and  peperoni == "y" and   cheese == "n":
    print("You should pay($20 + $2):$22")
elif size == "l"  and  peperoni == "y" and   cheese == "n":
    print("You should pay($25 + $2):$27")

# =-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

if size == "s"  and   peperoni == "n" and   cheese == "n":
    print("You should pay($10):$10")
elif size == "m"  and   peperoni == "n" and   cheese == "n":
    print("You should pay($20):$20")
elif size == "l"  and   peperoni == "n" and   cheese == "n":
    print("You should pay($25):$25")


input("Press enter to exit...")
