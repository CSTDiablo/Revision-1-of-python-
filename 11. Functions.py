# class definition

# class person():
#     pid=11
#     name="raj thapa"
#     address="kathmandu, nepal" #arguments of the class

# p= person() #object definition of the class


# print(p.pid,p.name,p.address) #calling the arguments of the class using object
# age = int(input("enter your age"))
# class check():
#     def __init__(self, age):
#         self.age= age
        
        
#     def eligible(self):
#         if self.age>16:
#             print("you are eligible ")
#         else:
#             print("you are not eligible")

# age = int(input("enter your age"))



# c = check(age) #object initialization
# c.eligible()
from unicodedata import name


class Check():
    def __init__(self, age, name):
        self.age= age
        self.name=name
    def getName(self):
        self.name = name
        return self.name
    def setAge(self):
        # self.age = age
        return self.age
        
    def eligible(self, age):
        # self.age = age
        if self.age>16:
            print("you are eligible ")
        else:
            print("you are not eligible")

age = int(input("enter your age"))

class Bus(Check):
    def vehicleeligible(self):
        # self.age=age
        if self.age>20:
            return "youre eligible"
        else:
            return "youre not eligible"


# c = Check(age) #object initialization
# c.eligible()

c2 = Bus(age,"John") #object initialization
print(c2.vehicleeligible())
print(c2.getName())
print(c2.setAge())

print("∞")