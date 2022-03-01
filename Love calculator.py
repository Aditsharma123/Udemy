from errno import E2BIG


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_in_lower = name1.lower()
name2_in_lower = name2.lower()
l=name1_in_lower.count("l")
o=name1_in_lower.count("o")
v=name1_in_lower.count("v")
e=name1_in_lower.count("e")

t=name1_in_lower.count("t")
r=name1_in_lower.count("r")
u=name1_in_lower.count("u")
e2=name1_in_lower.count("e")

# t  l
# r  o
# u  v
# e  e
# _  _%

unit_digit = l+o+v+e 
tens_digit = t+r+u+e2

print(f"probablity is {tens_digit}{unit_digit}%")