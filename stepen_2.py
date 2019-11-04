def stepen_2(x):
    while x > 1:
        if x%2 == 0:
            return stepen_2(x//2)
        else:
            x = 0
    if x == 1:
        return("YES")
    else:
        return("NO")
