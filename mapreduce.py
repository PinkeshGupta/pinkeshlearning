def sqr(a):
    return a*a

def cube(a):
    return a*a*a

func = [sqr,cube]


for  i in range(5):
    var = list(map(lambda x:x(i),func))
    print(var)