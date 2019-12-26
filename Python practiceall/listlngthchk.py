def strlng(listele):
    wrd= 0

    for i in listele:
        if len(i) >1 and i[0] == i[-1]:

            wrd +=1
    return wrd

print(strlng(['abc','xyz','aba','1221']))
