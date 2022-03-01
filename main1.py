# Challenge

# print(len(input("Enter your name: ")))


City_name = input("Please Enter Your City Name: \n")
Dog_name = input("Please enter your dog name: \n")
Dog_name += " "

print("Your Band name should be: " + Dog_name + City_name)

# challenge 2

height = float(input("Please enter your height(in m): "))
weight = float(input("Please enter your weight(in Kg): "))

height = height ** 2
BMI = weight / height
bmi = int(BMI)
print("BMI: ", bmi)
