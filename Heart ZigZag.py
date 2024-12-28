from sys import exit
import time 
indent = 0
width = 5
rigCount = 0
percentLove = 0
borderTouch = 0
y = 50
def zigzagA():
    global indent
    print(str(indent * ' ')  + str(percentLove) + '% '+ 'love for you ' + '❤️' * width )
    indent = indent + 1
def zigzagB():
    global indent
    print(str(indent * ' ')  + str(percentLove) + '% '+ 'love for you ' +  '❤️' * width )
    indent = indent - 1

try:
    while True:
        if rigCount == 1500:
                print(str(percentLove) + '% '+ 'love for you' )
                exit()
        elif indent < y + 1:
            zigzagA()
            rigCount = rigCount + 1
            time.sleep(0.1)   
            percentLove = percentLove + 1
            borderTouch = borderTouch + 0
        elif indent >= y:
            for i in range(1,y):
                zigzagB()
                time.sleep(0.1)
                rigCount = rigCount + 1
                percentLove = percentLove + 1
            borderTouch = borderTouch + 1
except KeyboardInterrupt:
    exit()