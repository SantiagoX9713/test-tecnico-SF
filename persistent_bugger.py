def persistence(n):
    if len(str(n)) == 1:
        return 0
    elif n > 0:
        s = str(n)
        steps = 0
        temp = 1
        while len(s) > 1:
            for i in s:
                temp *= int(i)
            s = str(temp)
            print(temp)
            steps += 1 
            temp = 1
        return steps
