class ParentClass:
    var1 = "I am var1"
    var2 = "I am var2"

    def whoami(self):
        return "I am object", self


class ChildClass(ParentClass):
    pass

parentObject = ParentClass()
print parentObject.var1
print parentObject.var2
print parentObject.whoami()

childObject = ChildClass()
print childObject.var1
print childObject.var2
print childObject.whoami()
