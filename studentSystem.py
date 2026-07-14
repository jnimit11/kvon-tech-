class Student:
    def __init__(self, name, rollNumber, marks):
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks
        
    def calculate_average(self):
        average = sum(self.marks) / len(self.marks)
        return average
    
    def display_result(self):
        average = self.calculate_average()
        
        if average >= 40:
            print("Result: PASS")
            
        else:
            print("Result: FAIL!!")
            
    def display_student(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.rollNumber}")
        print(f"Marks: {self.marks}")
        
        