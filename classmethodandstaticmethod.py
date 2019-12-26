class Employee:
    raise_amount =1.04
    num_of_emp = 0
    def __init__(self, first_name,last_name,pay):
        self.first_name =first_name
        self.last_name =last_name
        self.pay =pay
        self.email = first_name+ "." +last_name +"@company.com"

        Employee.num_of_emp +=1
    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount) :
        cls.raise_amount =amount
          
emp1 = Employee("Pinkesh","Gupta", 400000)
emp2 = Employee("Test","User", 25000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

