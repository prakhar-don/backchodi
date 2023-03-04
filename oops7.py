class employee:
    salary=1000
    increment=2

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment=sai/self.salary

prakhar=employee()
print(prakhar.salaryAfterIncrement)
print(prakhar.increment)
prakhar.salaryAfterIncrement=300
print(prakhar.increment)