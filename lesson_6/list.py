family = ['dad', 'mum', 'bro', 'sis']  # creates a list to store diff items

family[0]  # holds dad
family[1]  # holds mum
family[2]  # holds bro
family[3]  # holds sis

family[-1]  # holds sis minus -1 starts from the end of the list
family[-4]  # holds dad

family[0] = 'Grandpa'  # update the value at index 0 to Grandpa
del family[0]  # deltes Grandpa from the list
print family[-4] # prints dad

print family[0][1] #prints the first chracter in the string 'dad'



print len(family)  # prints the length of the family list 4


numbers = [10, 34, 90, 78, 21, 32, 320, 23]

max(numbers)  # prints the maximum number in the list
min(numbers)  # prints the minimum number in the list

list('Simon Peter')  # creates a list out of the string


def add_to_list():
    my_list = []
    while len(my_list) != 10:
        item = raw_input("Put an item in the list")
        my_list.append(item)

    print "Here are the items in your list", my_list






