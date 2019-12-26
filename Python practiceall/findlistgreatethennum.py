def listgrtnum(n,str):
    lstitem =[]
    txt =str.split(" ")
    for i in txt:
        if len(i)>n:
            lstitem.append(i)
    return lstitem
print(listgrtnum(4,"This is quick intro to my code here see"))
