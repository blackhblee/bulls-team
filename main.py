import random
import ckend
import play

def bullsAndCows():
    value = ''
    while True:
        if len(value) == 4:
            break
        ck = str(random.randint(0, 9))
        if ck not in value:
            value+=ck
    play.play()
    ckg = ckend()
    if ckg == '0':
        print('Quit game.')
    elif ckg == '1':
        print('Restart game.')
        bullsAndCows()
        return

bullsAndCows()
