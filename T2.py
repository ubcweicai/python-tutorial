myarr = [58114, 10, 3430, 632, 4222]
# x = int(input("pls enter value for the array "))

#for i in range(5):
#    myarr.append(x)


def sum_digit(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def leading(m):
    m = str(m)
    return int(m[0])


def weirdfilter(arr):
    """this is actually on our TO DO list to go through"""
    #arr = []
    print(arr)
    for i,number in enumerate(arr):
        if sum_digit(number) % 2 == 0 or leading(number) == len(str(number)):
            #number
            #pass
            arr[i]=number
        else: 
            arr[i]=-1
    return arr


print(weirdfilter(myarr))
