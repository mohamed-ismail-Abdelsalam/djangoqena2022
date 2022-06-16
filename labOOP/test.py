from Car import Car
from Employee import Employee
from Office import Office


Fiat128=Car('Fiat128',100,100)
samy=Employee('samy',50000,100,100,1,Fiat128,'samy@gmail.com',5000,100)
employees=[samy,Employee('sara',50000,100,100,2,Fiat128,'sara@gmail.com',5000,100)]
ITI=Office('ITI smart',employees)