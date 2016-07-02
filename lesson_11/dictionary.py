family = {'dad': 'bill gate', 'mum': 'melinda gate', 'son': 'simon peter gate'}

print family.values()
print family.keys()

print family['dad']
print family['mum']

'dad' in family  # checks if the dictionary have the key
family.has_key('dad') # checks if the dictionary have the key

new_family = family.copy()  # copies the content of family to new family

family.clear()  # wipes out everything in the dictionary