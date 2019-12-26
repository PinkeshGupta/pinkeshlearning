def minvallst(lstitm):
    minval =lstitm[0]
    for i in lstitm:
        if i < minval:
            minval = i
    return minval
print(minvallst([3,6,0,-8,7]))