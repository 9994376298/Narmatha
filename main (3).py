class student:

 def __init__(self,name,roll_number,cgpa):
   self.name= name
   self.roll_number= roll_number
   self.cgpa= cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key = lambda student: student.cgpa,reverse = True)
  return sorted_students

students =[
     student("durga", "A123", 7.8),
     student("kalai", "A124", 8.9),
     student("radhika", "A125", 9.1),
     student("abi", "A126", 9.9), 
] 
sorted_students =  sort_students(students)

   
#Print the sorted list ofstudent 

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format (student.name, 
                                                      student.roll_number, 
                                                      student.cgpa))
