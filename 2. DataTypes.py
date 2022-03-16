#DataTypes
    #bool
    #int
    #float
    #str

# 1. bool-boolean (true/false)

"""
On/Off
True/False
1/0
Yes/No
"""

import sys

"""
print(True)
print(False)
"""

"""
var1 = True #declare variable #assign value
print(var1) #access value of var1
"""

#type()
"""
var1 = True #declare and assign
print(type(var1)) #return the type of var1
var1 = False # Re-declare and assign
print(type(var1))
"""


#id() #return memory location of the variable
"""
var1 = True #declare and assign
print(type(var1)) #type of value in var1 #<'class bool'>
print(id(var1)) #Memory address #140723285773160
print(var1)# accessing the variable #true

var1 = False#Re-declare and assign
print(type(var1))
print(id(var1))
print(var1)
"""
#getsizeof() - shows how much memory space is occupied by a variable
"""
var1=True
print(sys.getsizeof(var1)) #28
"""

#all in one
"""
var1 = True
var2 = False
print(type(var1))
print(id(var1))
print(sys.getsizeof(var1))
print(type(var2))
print(id(var2))
print(sys.getsizeof(var2))

#python extra - we can find type, memory address and size of variables in single line of command
print(type(var1),type(var2)) #type
print(id(var1),id(var2)) #memory address
print(sys.getsizeof(var1), sys.getsizeof(var2)) #size
"""

#2. Integer Number
    #Numeric type- Whole number(without fractional value)
    #Add, Sub, Prd, Div, Pow, SQRT - operations
    #==,!=,>,>=,<,<= - operations
"""

num1 = 9801850298
print(num1) #access value
print(type(num1)) #type of value
print(id(num1)) #memory address of value
print(sys.getsizeof(num1)) #size of value

"""

#type conversion - process of converting one data type to another data  type 
    #str -> int
    #float -> int
    #bool -> int

#basic validation
    #isinstance() - checks whether the object or variable is an instance of the specified class type or data type

"""
var1 = 123
print(isinstance(var1, bool))
print(isinstance(var1, int))
print(isinstance(var1, float))
print(isinstance(var1, str))
"""

#3. Float - number with fractional values
    #Add, Sub, Prd, Div, Pow, SQRT - operations
    #==,!=,>,>=,<,<= - operations
"""
var1 = 123.456789
print(var1)
print(type(var1))
print(id(var1))
print(sys.getsizeof(var1))
print(isinstance(var1,float))
print(isinstance(var1,int))
print(isinstance(var1,str))
print(isinstance(var1,bool))
"""

# Extended Data Types
    # str
    # array
    # list
    # tuple
    # set
    # dictionary

#1. str (String)
# Representation
    # 'ABC'
    # "ABC"
    # '''ABC'''
    # """ABC"""

# Decalre
"""
str1 = 'ABC'
str2 = "ABC"
str3 = '''ABC'''
str4 = ""ABC""
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

str1 = "Broadway Infosys Nepal is one of the best inclusive computer training institutes in Kathmandu, Nepal. Established in 2008, our professional IT Training and Development center has been employing experts in this field to impart professional education."
print(str1)
print(type(str1))
print(id(str1))
print(isinstance(str1, str))
print(len(str1)) # 249
print(max(str1)) # Based on ASCII Value
print(min(str1)) # Based on ASCII Value
"""

# A-Z a-z 0-9 Symbols (Character Set)
# Each character have it unique number called ASCII Code

# Documentation of module/class
# print(help(str))
# print(dir(str))

