class vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
    
            str1+= f"{i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self,v):
        newlist=[]
        if len(self.vec)!=len(v.vec):
            print("vector cannot be added")
        else:    
            for i in range(len(self.vec)):
             newlist.append(self.vec[i] + v.vec[i])
        return vector(newlist)    

    def __mul__(self,v):
        sum=0
        for  i in range(len(self.vec)):
            sum+= self.vec[i]*v.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)


v1=vector([1,2,5])
v2=vector([6,9,0])
print(len(v1))
print(v1+v2)
