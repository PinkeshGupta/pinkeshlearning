def maxvallst(lstitm):
    maxval =lstitm[0]
    for i in lstitm:
        if i > maxval:
            maxval = i
    return maxval
print(maxvallst([3,6,0,-8,7]))