print("welcome to the rollercoaster")
height=int(input("enter your height :"))
if height>=120:
    print("you can ride")
    age=int(input("enter your age :"))
    if age<12:
        bill=5
        print("child ticket is 5/-")
    elif age<=18:
        bill=10
        print("adult ticket is 10/-")
    else:
        bill=20
        print("all other tickets are 20/-")
        
        want_photo=input("type yes or no :")
        if want_photo=="yes":
            bill+=3
            print(f"your final bill is {bill}")
else:
      print("sorry! your height is not enough to ride")