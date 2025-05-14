# Task 1

class Polygon:
    def __init__(self):
        self.number_of_sides = None
        self.side_length = None

class Rectangle(Polygon):
    def __init__(self, side_1, side_2):
        super().__init__()
        self.side_1 = side_1
        self.side_2 = side_2
        self.number_of_sides = 4

    def find_square(self):
        square = self.side_1 * self.side_2
        print(square)

r1 = Rectangle(2, 4)
r1.find_square()


# Task 2
class Human:
    def __init__(self, name):
        self.name = name
    def greet_all(self):
        print(f"Welcome,{self.name}!")

    @classmethod
    def homo(cls):
        print("This is an example of Homo Sapiens species.")

    @staticmethod
    def breed():
        print("Cross-species breeding is impossible.")

h1 = Human("Lera")
h1.greet_all()
Human.homo()
h1.breed()
Human.breed()


# Task 3
class Employee:
    """This is a simple Employee class."""
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def count_employees(cls):
        print(f"Currently there are {cls.count} employees.")

    def __str__(self):
        return f"Employee {self.name} earns {self.salary}."

e1 = Employee("Lera", 55000)
e2 = Employee("Nastya", 70000)

Employee.count_employees()
print(e1)

print("Base classes:", Employee.__bases__)
print("Namespace dict:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)

