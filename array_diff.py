def array_diff(a,b):
    for i in a:
        if i in b:
            a.pop(a.index(i))
    return a


if __name__ == '__main__':
    a = [0,1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,0]
    b = [1,3,5,7,9]
    print(array_diff(a,b)) 