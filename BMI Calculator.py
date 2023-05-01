weight = int(input("What is your weight in KG?: "))
height = float(input("What is your height in Meters?: "))
BMI = weight/(height**2)

if BMI<18.5:
    print("underweight")
elif (BMI>=18.5) and (BMI<25):
    print("normal")
elif (BMI>=25) and (BMI<30):
    print("overweight")
else: print("obese")