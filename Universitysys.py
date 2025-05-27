class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def display_info(self):
        return f"{super().display_info()}, Student ID: {self.student_id}, Major: {self.major}"

class Lecturer(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        return f"{super().display_info()}, Lecturer ID: {self.employee_id}, Department: {self.department}"

class Staff(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def display_info(self):
        return f"{super().display_info()}, Role: {self.role}"

# Testing the system
people = [
    Student("Alice", 20, "S1001", "Computer Science"),
    Lecturer("Dr. John", 45, "L2001", "Mathematics"),
    Staff("Mark", 38, "IT Support")
]

for person in people:
    print(person.display_info())
