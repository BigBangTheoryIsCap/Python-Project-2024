import time
print("Please enter text to be typed smoothly")
text = str(input())

for char in text:
    print(char, end = "", flush = True )
    time.sleep(0.1)
print()