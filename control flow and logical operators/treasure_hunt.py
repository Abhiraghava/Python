print(''' 
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
      ''')
print("welcome to treasure huntt")
print("your mission is to find the treasure")
choice1=input('you are in the land ,where you want to move "right"or "left".').lower()
if choice1=="right":
    choice2=input("you came to near to the lake,if you want to 'swim' or 'wait'.").lower()
    if choice2=="wait":
        choice3=input("you came to the room,choose any one colour and go.'green','red','blue'.")
        if choice3=="green":
            print("you won the game")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("you fall into the whole *game over*"  )