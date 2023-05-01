import random

def bullsAndCows():
    value = ''
    while True:
        if len(value) == 4:
            break
        ck = str(random.randint(0, 9))
        if ck not in value:
            value+=ck
    play()
    ckg = ckend()
    if ckg == '0':
        print('게임을 종료합니다.')
    elif ckg == '1':
        print('게임을 시작합니다.')
        bullsAndCows()
        return

