class Calculator:

    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"Square of {self.number} is {self.number**2} \n")    

    def squareRoot(self):
        print(f"Squareroot of {self.number} is {self.number**0.5} \n")    

    def cube(self):
        print(f"Cube of {self.number} is {self.number**3} \n")    

    @staticmethod
    def greet():
        print("*****Hello welcome to perfect Calculator******\n")  

three=Calculator(3)
three.greet()
three.square()
three.squareRoot()
three.cube()
          