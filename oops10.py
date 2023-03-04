class vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i+{self.vec[1]}j+{self.vec[2]}k"  
    def __add__(self,v):
        newlist=[] 
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+v.vec[i])
        return vector(newlist)         

v1=vector([0,12,2])
v2=vector([2,4,6])
print(v1+v2)