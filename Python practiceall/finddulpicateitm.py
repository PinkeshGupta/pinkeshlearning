def dup(itemd):
    duplicat = set()
    dlst=[]
    for i in itemd:
        if i not in duplicat:
            dlst.append(i)
            duplicat.add(i)
    return duplicat
print(dup([10,20,30,20,10,50,60,40,80,50,40]))


# list1 =[10,20,30,20,10,50,60,40,80,50,40]
# list2 = list(list1)
# print(list1)
# print(list2)