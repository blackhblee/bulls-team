def ckend():
    while True:
        ckg = input('게임종료(0), 시작(1): ')
        if ckg == '0':
            break
        elif ckg == '1':
            break
        else:
            print('잘못된 형식입니다.')
    return ckg
