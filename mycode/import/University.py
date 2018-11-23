class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def setname(self,name):
        self.name = name

    def setage(self,age):
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age


class Department:

    def __init__(self,name,code):
        self.name = name
        self.code = code

    def setname(self,name):
        self.name = name

    def setcode(self,code):
        self.code = code

    def getname(self):
        return self.name

    def getcode(self):
        return self.code
