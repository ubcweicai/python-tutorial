def f(x,y):
    coordinate = [0,0]
    dict = {'u':1,'d':-1,"l":-1,"r":1}
    for i in x:
        coordinate[1]=coordinate[1]+dict.get(i)
    for j in y:
        coordinate[0]=coordinate[0]+dict.get(j)

    return coordinate

print (f("uuud","rrrl"))
