import time

while True:
    print('Who are you?')
    userName = str(input())
    if userName !=  'Alok':
        continue
    print('What is the password?')
    userPass = str(input())
    if userPass == 'Korean Gum': 
        break
print('Access Granted')