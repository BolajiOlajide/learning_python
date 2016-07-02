print [1, 2, 3, 4] + [5, 6, 7, 8]  # adds two list
print 'simon' + 'peter'  # adds two sequence of text
print 'Hip ' * 2  # prints Hip Hip
print ['a'] * 10  # creates a ten times in new list
print [21] * 10  # creates 21 ten time in a new list

numbers = [1, 2, 3, 4, 5, 6]

numbers.insert(0, 'a')  # inserts the letter a to the start of the list

numbers.index('a')  # returns the index of the letter a in the list

numbers.pop(0)  # removes the first item in the list
numbers.pop()  # removes the last item in the list
numbers.remove(2) # removes the number two from the list
numbers.reverse() # revesre the list
numbers.sort() # sorts the list from smallest to biggest

2 in numbers  # returns True

0 in numbers  # returns False

name = 'simon'

'z' in name  # returns false

my_collection = ['apples', 'guava', 'grape', 'apples', 'grape']
print my_collection.count('apples')  # returns the number of occurrences of the word in the collection

my_collection.append('pear')  # adds the item pear to the end of the list note => appends only take one arg
my_collection.extend(['pants', 'socks', 'eraser'])  # adds the list to the my_collection list

print my_collection


