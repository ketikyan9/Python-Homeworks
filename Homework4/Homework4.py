
class Calculation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def addition(self):
        print(self.x + self.y)
    
    def subtraction(self):
        print(self.x - self.y)
        

class MyCalculation(Calculation):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def multiplication(self):
        print(self.x * self.y)
        
    def division(self):
        print(self.x / self.y)
        

my_cal = MyCalculation(3, 5)
my_cal.addition()
my_cal.subtraction()
my_cal.multiplication()
my_cal.division()


class My_Time:
    def __init__(self, t):
        self.t = t
        
    def printTime(self):
        print('The Current Time Is {}'.format(self.t))
        
class My_Date:
    def __init__(self, d):
        self.d = d
        
    def printDate(self):
        print('The Current Date Is {}'.format(self.d))
        
        
class Date_Time(My_Time, My_Date):
    def __init__(self, t, d):
        My_Time.__init__(self, t)
        My_Date.__init__(self, d)
        

time = Date_Time('12 PM', '13.03.2013')

time.printTime()
time.printDate()
