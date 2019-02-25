students=[]
passed=[]
fail=[]
s1=int(input("What is the mark for student 1?"))
students.append(s1)
s2=int(input("what is the mark for student 2?"))
students.append(s2)
s3=int(input("what is the mark for student 3?"))
students.append(s3)
s4=int(input("what is the mark fot student 4?"))
students.append(s4)
s5=int(input("what is the mark for student 5?"))
students.append(s5)
s6=int(input("what is the mark for student 6?"))
students.append(s6)
s7=int(input("what is the mark for student 7?"))
students.append(s7)
s8=int(input("what is the mark for student 8?"))
students.append(s8)
s9=int(input("what is the mark for student 9?"))
students.append(s9)
s10=int(input("what is the mark for student 10?"))
students.append(s10)
#print(students)

for marks in students:
    if marks>50:
        passed.append(marks)
    else:
        fail.append(marks)


'''print("The list of the students" + students)
print("The list of the students who passed the exam is " + passed)
print("The list of students who failed the exam is " + failed)'''

#x=len(students)
list_which_fail=len(fail)
list_which_passed=len(passed)
print("The list of students who failed is" + passed)
print("The list of students which passed" + fail)  


























































