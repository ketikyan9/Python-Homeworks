#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed
        
    def CompareCar(self, car2):
        if self.max_speed > car2.max_speed:
            return "car1 is better than car2"
        else:
            return "car2 is better than car1"

car1 = Car("BMW", "black", 31)
car2 = Car("Toyota", "white", 24)
print(car1.CompareCar(car2), '\n')

class Person:
    def __init__(self, name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password
    
    def Greeting(self, second_person):
        print("Welcome Dear", second_person.name)
        
    def Goodbye(self):
        print("Bye everyone!")
        
    def Favorite_num(slef, num1):
        return "My favorite number is " + str(num1)
    
    def Read_file(self, num1):
        with open(filename + 'txt', 'r') as f:
            print(f.read())
            
    def set_password(self, pwd):
        self.__password = pwd
        
    def get_password(self):
        return self.__password
    
person = Person("Mike", "Johnson", 21, 'M', True, "123123")
print(person.Favorite_num(12))
print("My password:", person.get_password())


# In[ ]:




