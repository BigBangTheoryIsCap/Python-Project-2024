friendNames = []
while True:
    print('Enter friend ' + str(len(friendNames)+1) +  ' to keep track, or nothing to stop:')
    friendName = input()
    if friendName == '':
        break
    friendNames = friendNames + [friendName] 
print('The friends names are:')
sorted_friendNames = sorted(friendNames)
for friendName in sorted_friendNames:
    print('  '+ friendName)

