def prdlist(itmlst):
    prdval =1
    for i in itmlst:
        prdval *= i
    return prdval

print(prdlist([4,5,8]))
            