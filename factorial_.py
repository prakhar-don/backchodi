def fact(num):
    if num==1 or num==0:
        return 1
    else:    
        return fact(num-1)*num

r=fact(1)
  
print(r)  
