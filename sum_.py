def sumN(num):
    if num==0:
        return 0
    else:
        return sumN(num-1)+num 
           
s=sumN(5)
print(s)
