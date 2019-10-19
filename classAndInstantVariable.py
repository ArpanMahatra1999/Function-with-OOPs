#defining a class variable name

class Edureka():
    domain = ("Data Science")
    def Setcourse(self, name):
        self.name = name

#defining instances

ob1 = Edureka()
ob2 = Edureka()

ob1.Setcourse("Python")
ob2.Setcourse("Machine Learning")

print(ob1.domain)
ob1.domain = "God"

print(ob1.domain)
print(ob2.domain)

print(ob1.name)
print(ob2.name)