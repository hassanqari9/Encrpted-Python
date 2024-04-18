# Multilevel Inheritance - When a class is derived from a class which is also derived from another class, i.e. a class having more than one parent class but at different levels, such type of inheritance is called Multilevel Inheritance.

class Manager:
    def __init__(self, v):
        self.value = v
    def review(self):
        print("Final Review")


class Tester(Manager):
    def review(self):
        print("Testing")


class Coder (Tester):
    def __init__(self, v):
       Manager.__init__(self, v)
       
    def writes(self):
        print("Writing Code")

w = Coder('pagl ho kya?')
# w.finalreview()
# w.review() # will call the method from the Inherited class ie, Tester
# w.writes()
print(w.value)
