print("welcome to pizza delivery site :")
print("choose the sizes s,m,l :")
size=input("what size do you want :")
add_pepperoni=input("Do you want pepperoni : ")
extra_cheese=input("Do you want extra cheese : ")

bill=0

if size=="s":
    bill+=15
elif size=="m": 
    bill+=20
else:
    bill+=25 
if add_pepperoni=="y":
    if size=="s":
     bill+=2
else:
     bill+=3
if extra_cheese=="y":
     bill+=1
                
print(f"your finall bill is :{bill}")
                 
