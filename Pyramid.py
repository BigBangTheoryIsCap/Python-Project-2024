while True:
    print('How many rows would you like?')
    rowCount = int(input())
    indent = rowCount
    rowLength = 2
    while rowCount > 23 or rowCount == 0:
        print('Enter a number less than 23, and greater than 0')
        rowCount = int(input())
    while rowLength < rowCount + 2:
        for i in range(0,indent):
            print('  ', end = '')
        for x in range(0, rowLength):
            print('#', end = '')
            print(' ' , end = '')
        print(' ')
        indent = indent - 1
        rowLength = rowLength + 1