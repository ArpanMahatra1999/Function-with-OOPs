class Edureka:
    def __init__(self, courseName):
        self.courseName = courseName

    def setCourseName(self, courseName):
        self.courseName = courseName

    def getCourseName(self):
        return(self.courseName)

ob = Edureka("Python")
print(ob.getCourseName())

ob.setCourseName("Machine Learning")
print(ob.getCourseName())