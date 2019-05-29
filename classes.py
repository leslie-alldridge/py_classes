class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount


emp_1 = Employee(first='Leslie', last='Alldridge', pay=123)
emp_2 = Employee(first='Leslie2', last='Alldridge2', pay=2)

Employee.set_raise(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)