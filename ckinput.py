def ckinput():
    while True:
        exValue = input('4자리 숫자를 입력하세요: ')
        
        if not len(exValue) == 4:
            print("형식에 맞지 않는 숫자입니다. 다시 입력해주세요.")
            continue
        
        if not len(set(exValue)) == 4:
            print("중복된 숫자가 있습니다. 다시 입력해주세요.")
            continue
            
    return exValue