class Student:
  
  def __init__(self,name,roll_no,cgpa):
    self.name=name
    self.roll_no=roll_no
    self.cgpa=cgpa
    
def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student: student.cgpa,
                         reverse=True)
  return sorted_students
  
students=[Student("Hari","a123",7.8),Student("ashwin","a234",9.0), Student("madhu","s232",4.3)]

  
sorted_students=sort_students(students)
for student in sorted_students:
    print(student.name,student.roll_no,student.cgpa)    
        