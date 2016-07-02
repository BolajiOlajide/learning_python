age = input("Please enter your age: ")

if (age >= 13)and (age <= 19):
    print "You are still a teenager"
elif (age >= 20) and (age <= 26):
    print "You are a young adult"
elif (age >= 27) and (age <= 39):
    print "You are an adult"
elif (age >= 40) and (age <= 59):
    print "You are really matured"
elif age >= 60:
    print "You are too old"
else:
    print "You are still a kid"


thing = "house"
animal = "cat"

if thing == "animal":
    if animal == "cat":
        print 'this is a cat'
    else:
        print "I don't know what animal is this"
else:
    print "I don't know what this thing is"

10 == 10  # True
9 != 9   # False
9 != '9'  # True

9 > 2  # True
2 < 9  # True

one = [1, 2, 3, 4, 5]
two = [1, 2, 3, 4, 5]

print one is two  # False because they are different object

four = three = two  # multiple assignment

if 's' in 'Zebra':
    print "That's weird or are there several Zebras?"
