class student:

    def __init__(self,name,age):
        print("Student object created with name = %s and age = %s" %(name,age))
        self.name = name
        self.age = age

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setage(self, age):
        self.age = age

    def getage(self):
        return self.age

    def __del__(self):
        print("object destroyed")

st = student("Lokesh","30")

