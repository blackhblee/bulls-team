import ckinput()

def play():
    turn = 1
    while True:
        if turn == 11:
            print('입력횟수가 초과됐습니다. Game Over','정답: ',value)
            break

        exValue=ckinput()
        if value == exValue:
            print(exValue, '정답입니다.', '턴수:', turn)
            break

        b = 0
        c = 0
        for s in range(len(exValue)):
            if exValue[s] == value[s]:
                b+=1
            elif exValue[s] in value:
                c+=1
        print('판정:{}B{}C  턴수:{}\n'.format(b,c,turn))
        turn+=1
