import datetime


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
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--> ' + emp.fullname())


dev_1 = Developer(first='Leslie1', last='Alldridge1',
                  pay=22, prog_lang="JavaScript")
dev_2 = Developer(first='Leslie2', last='Alldridge2', pay=20, prog_lang="Java")


mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

print(mgr_1.email)
mgr_1.print_emps()

print(issubclass(Developer, Employee))

emp_1 = Employee('test', 'test2', 90)
emp_2 = Employee('test', 'test2', 90)

print(str(emp_1))
print(repr(emp_1))
print(emp_1 + emp_2)
print(len(emp_1))
