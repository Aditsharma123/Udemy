# taking height and weight
height = float(input("Enter your height(in m): "))
weight = float(input("Enter your weight(in kg): "))

height = height**2

BMI = round(weight/height, 2)

if BMI < 18.5:
    print(f"Your BMI is: {BMI},(BMI upto 18.5 is considered underweight) you are under weight")
elif 18.5 < BMI < 25:
    print(f"Your BMI is: {BMI},(BMI between 18.5 and 25 is considered as normal weight) you have a normal weight")
elif 25 < BMI < 30:
    print(f"Your BMI is: {BMI},(BMI beteen 25 and 30 is considerd as overweight) you are overweight weight")
elif 30 < BMI < 35:
    print(f"Your BMI is: {BMI},(BMI between 30 and 35 is considerd as obess) you are obsessed")
elif 35 < BMI:
    print(f"Your BMI is: {BMI},(BMI above 35 is considered as clinically obessed) you are clinically obsessed")
