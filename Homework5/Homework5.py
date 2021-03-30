# prob 1
def div(x, y):
    assert y != 0, "can't divide"
    return x/y

div(1, 0)

# prob 2
x = ['a', 0, 2]

for i in x:
    print("The entry is:", i)
    try:
        print("The reciprocal of", str(i), " is", str(1/i))
    except Exception as error:
        print("Oops!", error)

# prob 3
class Person:
    def __init__(self, name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        assert(student == 0 or student == 1), "Exception thrown, not a boolean value."
        self.student = student
        self.__password = password
    
    def Greeting(self, second_person):
        print("Welcome Dear", second_person.name)
        
    def Goodbye(self):
        print("Bye everyone!")
        
    def Favorite_num(slef, num1):
        try:
            return "My favorite number is " + str(int(num1))
        except:
            return "No valid number"
    
    def Read_file(self, filename):
        try:
            with open(filename + '.txt', 'r') as f:
                print(f.read())
        except Exception as error:
            print(error)
            
    def set_password(self, pwd):
        self.__password = pwd
        
    def get_password(self):
        return self.__password
    
person = Person("Mike", "Johnson", 21, 'M', True, "123123")
print(person.Favorite_num("1s2"))
print("My password:", person.get_password())
print(person.Read_file("AAA"))
