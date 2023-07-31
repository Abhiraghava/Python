year=int(input("which year do you want to cheack? :"))

if(year%4==0 and year%100!=0 or year%400==0 ):
    print("its a leap year")
else:
    print("it is not a leap year")