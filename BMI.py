print("Welcome to the BMI Calculator")

height = float(input('Please Enter you Height in Meters: \n'))

weight = float(input("Please Enter your Weight in Kilograms: \n"))

bmi = weight/(height**2)

bmi = round(bmi,1)

bmi = str(bmi)

print("Your BMI is " + bmi + "\n")

bmi = float(bmi)

if(bmi < 16):
    print("You are severly underweight")
elif(bmi >= 16 and bmi < 18.5):
    print("You are underweight")
elif(bmi >= 18.5 and bmi < 25):
    print("You are Healthy")
elif(bmi >= 25 and bmi < 30):
    print("You are overweight")
elif(bmi >= 30):
    print("You are severly overweight")