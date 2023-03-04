def maxThree(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            print(f"{num1} is the greaetest ")
        else:
            print(f"{num3} is the greatest")    
    elif(num2>num3) :
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest") 

result=maxThree(1,4,3)
print(result)

