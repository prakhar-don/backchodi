class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary+c.imaginary)
       
    #def __str__(self):
        return f"{self.real}+{self.imaginary}i" 
    def __sub__(self,c):
        return Complex(self.real-c.real,self.imaginary-c.imaginary)       
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"    
c1=Complex(2,3)
c2=Complex(4,1)
print(c1+c2) 
print(c2)         