# Super Class 'Employee'
import math


class Employee:
    def __init__(self, identity, name):
        self.identity = identity
        self.name = name


# Class 'HourlyEmployee' inherits from 'Employee'
class HourlyEmployee(Employee):
    def __int__(self, identity, name, hourly_pay, hours_worked):
        super().__init__(identity, name)
        self.hours_worked = hours_worked
        self.hourly_pay = hourly_pay

    def hour(self):
        hourly_pay = self, self.hours_worked * self.hours_worked
        print("Hourly Salary")
        print("ID No.", self.identity)
        print("Name", self.name)
        print("Hourly salary is:", hourly_pay)
        return


# Class 'SalaryEmployee' from 'Employee'
class SalaryEmployee(Employee):
    def __int__(self, identity, name, basic_salary, allowance):
        super().__init__(identity, name)
        self.basic_salary = basic_salary
        self.allowance = allowance

    def calculate_payroll(self):
        pay = self.basic_salary + self.allowance
        print(self.name)
        print(self.identity)
        print(pay)
        return


# Class 'CommissionEmployee' inherits from 'SalaryEmployee'
class CommissionEmployee(SalaryEmployee):
    def __init__(self, identity, name, basic_salary, commission_per_sale, allowance):
        super().__init__(identity, name, basic_salary, allowance)
        self.commission_per_sale = commission_per_sale

    def calculate_payroll(self):
        commission = (self.basic_salary + self.allowance)
        print("Commission")
        print("ID No.", self.identity)
        print("Name", self.name)
        print("Total commission is:", math.trunc(commission))
        return


employee = SalaryEmployee(3567, 'Gen', 2400, 1100)
employee.calculate_payroll()
hooray = HourlyEmployee(13840, 'Eugine', 2600, 700)
hooray.hour()
Commas = CommissionEmployee(3567, 'hei', 5400, 1200, 50)
Commas.calculate_payroll()


