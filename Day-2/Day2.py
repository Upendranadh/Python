# 
# *Data Types

#
#strings
print("Hello"[3])
print("123"+"456")

#integer
print(123+456)

#Float
print(3.10+2.25)

#Boolean

True
False

# len function
# len function only works with strings

print(type(2))
print(type("Hello"))

# type conversion 

print(int("120")+float("12"))
print(str(100)+str(120))
print(float(2),int(2.4))



# Mathematical operations

# order of priority
# PEMDAS
# Paranthesis()
# Exponents(**)
# Multiplication(*)
# Division(/)
# Addition(+)
# Substraction(-)

print(3 * 3 + 3 / 3 - 3)

# Example


# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")


# #Write your code below this line 👇

# int_height=float(height)
# int_weight=float(weight)
# BMI =int_weight/int_height**2
# print(int(BMI))


#Mathematical Functions

print(round(4.56))
print(round(4.56,1))

print(8/3)
print(8//3)

# f-string
# with out using + symbol and type converison to print differnt datatypes
name="Babi"
age=25
boolean=True

print(f"My name is {name} and age is {age} and Boolean is {boolean}")