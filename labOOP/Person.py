class Person:
    moods=('happy', 'tired', 'lazy')
    def __init__(self,name, money, mood, healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.__healthRate=healthRate
    @property
    def healthRate(self):
        return self.__healthRate
    @healthRate.setter
    def healthRate(self,newhealthRate):
        if(newhealthRate in [100,75,50]):
            self.__healthRate=newhealthRate
        else:
            print('invalid healthRate')
    def sleep(self,hours):
        if(hours>7):
            self.mood=Person.moods[2]
        elif (hours <7):
            self.mood = Person.moods[1]
        else:
            self.mood = Person.moods[0]
    def eat(self,meals):
        if(meals==3):
            self.__healthRate=100
        elif (meals == 2):
            self.__healthRate = 75
        elif (meals == 1):
            self.__healthRate = 50
    def buy(self,items):
        self.money-=items*10

