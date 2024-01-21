class User:

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self) -> str:
        return f"Name is: {self.name}, Age is: {self.age}, GPA is: {self.gpa}"
    

stud1 = User(age=23, gpa=3.5, name="Kim")

print(stud1)