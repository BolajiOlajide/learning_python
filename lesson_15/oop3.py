class Mom:
    var1 = "hey I am mom"

class Dad:
    var2 = "hey I am dad"

    def whoami(self):
        return 'I am dad'

# multiple inheritance from a parent class 
class Child(Mom, Dad):
    var3 = "hey I am child"

    def whoami(self):
        return 'I am child'
childObject = Child()

print childObject.var1
print childObject.var2
print childObject.var3
print childObject.whoami()