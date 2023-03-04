num=int(input("Enter the input:\t "))
prime=True
for i in range(2,num+1):
    if(num%i==0):
        prime=False
        break
            

if prime:
    print("The number is prime")
else:
        print("The number is not prime")
