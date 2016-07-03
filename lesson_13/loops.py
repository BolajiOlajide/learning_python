spell = 10

while spell > 0:
    spell -= 1
    if spell == 0:
        print 'casting my LAST spell'
    else:
        print 'casting spell....'

items = ['bread', 'apple', 'pants', 'socks', 'noodles']

for item in items:
    print item

menus = {'break_fast': ['eggs', 'tea', 'cashew'], 'lunch': ['fried rice', 'chicken', 'sauce'],
         'dinner': ['fufu', 'vegetables']}

for food in menus:
    print menus[food]


# infinite loop

while True:
    name = raw_input('Enter a name: ')
    if name == 'quit':
        break

