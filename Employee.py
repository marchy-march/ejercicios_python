class Employee:
    _name = None 
    _salary = None
    _CURP = None 
    def __init__(self,name_2,salary_2,CURP_2):
        self._name = name_2
        self._salary = salary_2
        self._CURP = CURP_2
    def sad_salary(self):
        if (self._salary < 30000):
            return(":c")
        else:
            return("c:")
    def set_salary(self, new_salary):
        self._salary = new_salary
        
    def get_salary(self):
        return(self._salary)

employee_1 = Employee("Marcia",4000,"MPJV345678")
print(employee_1._name)
print(employee_1._salary)

print(employee_1.sad_salary())
employee_1.set_salary(45000)


print(employee_1._name)
print(employee_1.get_salary())