# Define a class named Student
class Student:
    # Constructor: This method is called when an object is created
    def __init__(self, name, grade):
        self.name = name      # 'self.name' is an instance variable storing the student's name
        self.grade = grade    # 'self.grade' stores the student's grade

    # Method to display student info
    def display_info(self):
        # This method prints the name and grade of the student
        print(f"Name: {self.name}, Grade: {self.grade}")


# Create first object of Student class
s1 = Student("Praveen", "A")  # 's1' is an object with name "Praveen" and grade "A"

# Create second object of Student class
s2 = Student("Kumar", "B")    # 's2' is an object with name "Kumar" and grade "B"

# Call the method using both objects
s1.display_info()  # Output: Name: Praveen, Grade: A
s2.display_info()  # Output: Name: Kumar, Grade: B
