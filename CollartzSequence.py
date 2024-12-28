
import time, sys

def collartz():
    global num
    if num % 2 == 0 :
        num = num // 2
        print(int(num))
    else:
        num = 3 * num + 1
        print(int(num))
while True:
    try:
        print('Enter Number to run in sequence')
        num = int(input())
        print('Please enter itteration attempts')
        test = int(input())
        for i in range(1, test):
            collartz()
            time.sleep(0.1)
    except ValueError:
        print('Please enter a integer')
        continue
    print('Do you want to continue testing, or (q)uit')
    killSwitch = input()
    if killSwitch == 'q':
        break
        
