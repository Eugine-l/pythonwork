# Super Class 'Employee'
class Employee:
    def _init_(self,id,name):
        self.id=id
        self.name=name

# Class 'HourlyEmployee' inherits from 'Employee'
class HourlyEmployee(Employee):
    def _int_(self,id,name,hourly_pay,hours_worked):
        self.hours_worked=hours_worked
        self.hourly_pay=hourly_pay
        super(). _init_(id,name)
    def calculatepayroll(self,hours_worked,hourly_pay):
        return hours_worked*hourly_pay

# Class 'SalaryEmployee' from 'Employee'
class SalaryEmployee(Employee):
     def _int_(self,basic_salary,allowance):
         self.basic_salary=basic_salary
         self.allowance=allowance
         super()._init_(id,name)
    def employeesalary(self,basic_salary,allowance)
        return basic_salary*allowance

# Class 'CommissionEmployee' inherits from 'SalaryEmployee'
class CommissionEmployee(Salary_Employee):
    def _init_(self,commission_per_sale,number_of_sales):
        self.commission_per_sale=commision_per_sale
        self.number_of_sales=number_of_sales
        super()._init_(id,name,allowance,basic_salary)
    def employeecommission(self,commission_per_sales,number_of_sales):
        return commission_per_sales*number_of_sales





