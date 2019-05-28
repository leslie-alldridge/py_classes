class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee(first='Leslie', last='Alldridge', pay='123123')
emp_2 = Employee(first='Leslie2', last='Alldridge2', pay='2')

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Leslie'
# emp_1.last = 'Alldridge'
# emp_1.pay = '123123'
# emp_1.email = 'test@gmail.com'

# emp_2.first = 'Leslie2'
# emp_2.last = 'Alldridge2'
# emp_2.pay = '12'
# emp_2.email = '22test@gmail.com'

print(emp_1.email)
print(emp_2.email)