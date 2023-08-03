student_height=input("list of students :").split()
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)
total_height=0
for height in student_height:
    total_height+=height
print(total_height)
no_students=0
for students in student_height  :
    no_students+=1
print(no_students)
avg=round(total_height/no_students)
print(avg)    
