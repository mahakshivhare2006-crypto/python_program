"""1. Student Marks Analyzer Given a list of student marks, write a Python program to calculate and display:
 • Total marks 
 • Average marks 
 • Highest marks
   • Lowest marks 
   • Number of students who passed 
   • Number of students who failed"""
student_marks=[]
student_marks.append(int(input("Enter a Marks : ")))
student_marks.append(int(input("Enter a Marks : ")))
student_marks.append(int(input("Enter a Marks : ")))
student_marks.append(int(input("Enter a Marks : ")))
student_marks.append(int(input("Enter a Marks : ")))

#all student
all_students=len(student_marks)
print("number of all students :" ,all_students)

#total marks
total_marks=100
print("total marks :" ,total_marks)

#final marks
final_marks= sum(student_marks)
print("final marks :" ,final_marks)

#average marks
average_marks= final_marks/all_students
print("average marks :" ,average_marks)

#highest marks
highest_marks= max(student_marks)
print("highest marks :" ,highest_marks)

#lowest marks
lowest_marks= min(student_marks)
print("lowest marks :" ,lowest_marks)

pass_student=0
fail_student=0
for marks in student_marks:
    if marks>=40:
        pass_student+=1
    else:
        fail_student+=1


print("Number of students who passed " ,pass_student)
print("Number of students who failed " ,fail_student)