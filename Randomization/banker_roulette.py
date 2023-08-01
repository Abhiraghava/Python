import random
name_string=input("enter everybody's names :")
names=name_string.split(",")
pick=random.choice(names)
print(f"you have to pay the bill : {pick}")

