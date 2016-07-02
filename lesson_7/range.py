numbers = [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print numbers[0: 5]  # starts from 0 prints down to 17

print numbers[1: 10]  # starts from 20 prints down to 12

print numbers[2:5]  # starts at 19 prints down to 18

print numbers[0:10:2]  # starts at 21 down to 13 skip 2

print numbers[-10:]  # starts backward from 10 and prints to the end

print numbers[-3: -1]  # starts from backward from 3 and prints to the end

print numbers[10:0:-2]  # starts from the uppermost down up and counts backward skip 2

print numbers[:10]  # starts from 0 down to index 9

print numbers[::-2]  # starts from the last item on the list and counts backward skip 2