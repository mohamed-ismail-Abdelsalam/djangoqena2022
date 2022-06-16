from Person import Person
from re import fullmatch
class Employee(Person):
    emailpatterna='^[a-zA-Z][a-zA-Z0-9]+@{1}[a-zA-Z]{2,}[.]{1}[a-zA-Z]{2,4}$'
    def __init__(self, name, money, mood, healthRate,id , car, email, salary, distanceToWork):
        super(Employee,self).__init__(name,money,mood,healthRate)
        self.id = id
        self.car = car
        self.__email = email
        self.__salary= salary
        self.distanceToWork = distanceToWork

    @property
    def Salary(self):
        return self.__salary
    @Salary.setter
    def Salary(self, newsalary):
        if (newsalary >=1000):
            self.__salary = newsalary
        else:
            print('invalid salary')

    @property
    def Email(self):
        return self.__email

    @Email.setter
    def Email(self, newemail):
        if (fullmatch(pattern=Employee.emailpatterna,email=newemail)):
            self.__email=newemail
        else:
            print('invalid email')

    def work(self,hours):
        if (hours > 8):
            self.mood = Person.moods[2]
        elif (hours < 8):
            self.mood = Person.moods[1]
        else:
            self.mood = Person.moods[0]

    def drive(self,distance):
        self.car.run(distance,self.car.velocity)

    def refuel(self,gasAmount = 100):
        self.car.fuelRate+=gasAmount

    def send_mail(self,to, subject, msg, receiver_name):
        pass
