class programmer:
    company="Microsoft"
    def __init__(self, name,designation):
        self.name=name
        self.designation=designation

    def infoDo(self):
        print(f"Name of programmer is {self.name} and designation is {self.designation} \n")   

    @staticmethod
    def greet():
        print(f"***** Hello welcome to {programmer.company} ****** \n")    

        
Prakhar=programmer("Prakhar","data analyst")
Netrapal=programmer("Netrapal","software developer")
Prakhar.greet()
Prakhar.infoDo()
Netrapal.infoDo()




