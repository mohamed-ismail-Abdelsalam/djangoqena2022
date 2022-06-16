class Car:
    def __init__(self,name, fuelRate, velocity):
        self.name=name
        self.__fuelRate=fuelRate
        self.__velocity=velocity

    @property
    def FuelRate(self):
        return self.__fuelRate
    @FuelRate.setter
    def FuelRate(self, newfuelRate):
        if (newfuelRate>0 and newfuelRate<=100):
            self.__fuelRate = newfuelRate
        else:
            print('invalid healthRate')

    @property
    def Velocity(self):
        return self.__velocity

    @Velocity.setter
    def Velocity(self, newvelocity):
        if (newvelocity > 0 and newvelocity <= 100):
            self.__velocity = newvelocity
        else:
            print('invalid velocity')


    def run(self,velocity, distance):
        d=distance/velocity
        self.fuelRate=self.fuelRate-(d*10/100)

    def stop(self):
        self.velocity=0
        print('car stopped')