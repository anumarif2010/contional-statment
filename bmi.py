height =float(input("enter the height in cm :"))
weight =float(input("enter the weight in kg :"))

BMI=weight/(height/100)**2

print("your BMI is",BMI)
if BMI<=18.4:
    print("your aare under weight.")
elif BMI <=24.9:
    print("your in normal weight.")
elif BMI<=29.9:
    print("your over weight")
else:
    print("your obese")