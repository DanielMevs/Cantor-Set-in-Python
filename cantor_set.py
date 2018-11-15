def cantor(ls=[(0,1)]):
    from functools import reduce
    third = lambda interval: (interval[1]-interval[0])/3
    while True:
        yield ls
        ls = [[(k[0],k[0]+third(k)), (k[1]-third(k),k[1])] for k in  ls]
        ls = reduce(lambda x,y:x+y,ls)
            
g = cantor()
for i in range(6):
    print(next(g))
