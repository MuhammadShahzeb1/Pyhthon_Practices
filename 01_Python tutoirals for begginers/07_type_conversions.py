x=10
y=10.2
z="Hello"
# type() is used check the variable datatypes i.e int,float,str
print(type(x))
print(type(y))
print(type(z))

# Implicit type conversion
x=x*y  #it will automatically convert into float as integere multiply/devide/add/subtract with float is always equal to float
print(x)
print(type(x))

# explicit type conversion
age=input("what is your age? ")
age=float(age)
print(age, type(age))  
# if we put age in an float datatype it will give invalid output

name=input("what is your name? ")
name=str(name)
print(name,type(name))
# Note: amy number is also considered as string if its data type is not converted into int or float etc.
# Imp point : we have to design our programs according to the requiements for examole if age etc are required than use float ans similarly if required than use strings
#  

