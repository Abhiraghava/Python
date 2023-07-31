print("welcome to the love calculator :")
name1=input("enter your name : \n")
name2=input("enter the other name : \n")
combine=name1+name2
low=combine.lower()
t=low.count("t")
r=low.count("r")
u=low.count("u")
e=low.count("e")
true=t+r+u+e
l=low.count("l")
o=low.count("o")
v=low.count("v")
e=low.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if(love_score < 10) or (love_score > 90):
    print(f"your love score is :{love_score},you can proceed")
elif(love_score >= 40) and (love_score <= 50):
    print(f"your love score is:{love_score},your love is ok")
else:
    print(f"your love score is :{love_score},made for each other ><")
