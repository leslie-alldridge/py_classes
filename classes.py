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
    
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_str_1 = 'Leslie-Alldridge-2042'

emp_1 = Employee.from_string(emp_str_1)
emp_2 = Employee(first='Leslie2', last='Alldridge2', pay=2)

Employee.set_raise(1.05)

#print(Employee.raise_amount)
print(emp_1.email)
print(emp_2.raise_amount)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))