student_score=input("enter a list of student score : ").split()
for n in range(0,len(student_score)):
    student_score[n]=int(student_score[n])
print(student_score)
highest_score=0
for highest in student_score:
 if highest > highest_score:
       highest_score=highest
print(f"the highest score is :{highest_score}")            
         
