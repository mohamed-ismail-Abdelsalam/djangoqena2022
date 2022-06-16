from  Person import Person
class Office:
    employeesNum=0
    @classmethod
    def change_emps_num(cls,num):
        Office.employeesNum = num
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        Office.change_emps_num(len(self.employees))

    def get_all_employees(self):
       return  self.employees

    def get_employee(self,empId):
        for emp in self.employees:
            if(emp.id==empId):
                return emp

    def hire(self,empobject):
        self.employees.append(empobject)
        Office.change_emps_num(len(self.employees))

    def fire(self,empobject):
        self.employees.remove(empobject)
        Office.change_emps_num(len(self.employees))

    def deduct(self,empId, deduction):
        for emp in self.employees:
            if (emp.id == empId):
                emp.Salary=emp.Salary-deduction
    def reward(self,empId, reward):
        for emp in self.employees:
            if (emp.id == empId):
                emp.Salary = emp.Salary + reward

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time=distance/velocity
        if(moveHour+time<=targetHour):
            return True
        else:
            return False
    def check_lateness(self,empId, moveHour):
        for emp in self.employees:
            if (emp.id == empId):
                if(Office.check_lateness(9.00,moveHour,emp.distanceToWork,emp.car.velocity)):
                    self.reward(empId,10)
                else:
                    self.deduct(empId, 10)