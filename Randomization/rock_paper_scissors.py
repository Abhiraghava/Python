import random
print("welcome to rock-paper-scissors game ")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
games=[rock,paper,scissors]

choose=int(input("choose any one among this'rock(0)','paper(1)','scissors(2), you choose : "))


if choose>=3 :
 print("you entered an invalid number")
else:
 print(games[choose])
 random_pick=random.randint(0,2)
 print("computer choose :")
 print(games[random_pick])
 if choose==0 and random_pick==2:
    print("you won!")
 elif random_pick==0 and choose==2:
    print("you loose!")
 elif choose>random_pick:
  print("you won!")
 elif random_pick>choose:
  print("you loose!")
 elif choose==random_pick:
  print("its a draw!")




 


  