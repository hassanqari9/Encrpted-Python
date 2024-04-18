# Multiple Inheritance - Method Resolution Order (MRO) means the order in which the base classes are called in the event of multiple inheritance.

class Employee:
    def __init__(self, test):
        self.e = test

    def details(self):
        print(f"The Employee is {self.t}")

class Coder:
    def __init__(self, test):
        self.c = test

    def details(self):
        print(f"The known language is {self.t}")

class Programmer(Employee, Coder):
# class Programmer(Coder, Employee):       
    def __init__(self, language, name, test):
        super().__init__(test)
        self.language = language
        self.name = name

p = Programmer("Python", "Asif", "Test")
print(p.e)
# print(p.language)

# p.details() # The method from the first class will always be called

# print(Programmer.mro()) # Method Resolution Order (MRO) means the order in which the base classes are called in the event of multiple inheritance. This will give the order in which the base classes are called in the event of multiple inheritance.