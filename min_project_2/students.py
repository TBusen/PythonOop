class MusicSchool:
 
    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
		    "Talina": [28, "555-765-452", ["Cello"]],
		    "Eric":   [12, "583-356-223", ["Singing"]]}

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
 
    # Add your methods below this line

    def print_student(self, student):
        student = student
        age = MusicSchool.students.get(student)[0]
        classes = MusicSchool.students.get(student)[2]
        #phone_number = students.get(students)[1]
        print(f"Student: {student} who is {age} years old and is taking {classes}")
    
    def print_students_data(self):
        for student in MusicSchool.students:
            self.print_student(student)

    def add_student(self, student, data):
        student = student
        MusicSchool.students['student'] = data
        print("data added to students")



 
# Create the instance
 
s = MusicSchool(8, 15000)
 
# Call the methods

s.print_students_data()