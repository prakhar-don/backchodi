num=[5,3,6,9,4,10,1]
a=list(map(lambda x:x**3,num))
print("function of map")
print(a)

b=list(filter(lambda x:x>5,num))
print("function of filter")
print(b)

def square(n):
    return n*n

def cube(n):
    return n*n*n

func=[square,cube]

for i in range(4):
    val=list(map(lambda x:x(i),func))
    print(val)