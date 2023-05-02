import ckinput

def play():
    turn = 1
    while True:
        if turn == 11:
            print('Exceding the number of inputs. Game Over','Answer: ',value)
            break

        exValue=ckinput.ckinput()
        if value == exValue:
            print(exValue, 'Correct.', 'Turn:', turn)
            break

        b = 0
        c = 0
        for s in range(len(exValue)):
            if exValue[s] == value[s]:
                b+=1
            elif exValue[s] in value:
                c+=1
        print('Judge:{}B{}C  Turn:{}\n'.format(b,c,turn))
        turn+=1
