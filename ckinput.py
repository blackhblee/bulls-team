def ckinput():
    while True:
        exValue = input('Input 4 digit number: ')
        
        if not len(exValue) == 4:
            print("Wrong type of number. Try again.")
            continue
        
        if not len(set(exValue)) == 4:
            print("Duplicate number exist. Try again.")
            continue
        
        return exValue