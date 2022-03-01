year = int(input("Which year you want to check for: "))
if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!! :-) ")
        else:
            print("It's not a leap year :-( ")
    else:
        print("It's not a leap year :-( ")
else:
    print("It's not a leap year :-( ")
