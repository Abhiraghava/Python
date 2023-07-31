height=float(input("enter your height :"))
weight=float(input("enter your weight :"))
bmi=round(weight/height**2)
if(bmi<=18.5):
    print("underweight")
elif(bmi>18.5 and bmi<=25):
    print("you are in a normal weight")
elif(bmi>25 and bmi<=30 ):
    print("you are over weight")
elif(bmi>30 and bmi<=35):
    print("you are obese")
else:
    print("they are clinically obses")