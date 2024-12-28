import random

def pAnswer(nAnswer):
    if nAnswer == 1:
        return 'It is certain!'
    elif nAnswer == 2:
        return 'It is decidedly so!'
    elif nAnswer == 3:
        return 'Yes!'
    elif nAnswer == 4:
        return 'Reply hazy, try again!'
    elif nAnswer == 5:
        return 'Ask again later'
    elif nAnswer == 6:
        return 'Concentrate and ask again.'
    elif nAnswer == 7:
        return 'My reply is No'
    elif nAnswer == 8:
        return 'Outlook not so good'
    elif nAnswer == 9:
        return 'Very Doubtful'
    
r = random.randint(1,9)
Fortune = pAnswer(r)
print(Fortune)