def array_diff(a,b):
    for i in a:
        if i in b:
            a.pop(a.index(i))
    return a