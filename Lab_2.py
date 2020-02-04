#Wilson Song
#Afternoon 1

import math

#Function for question A -> receive a number *60 to convert to seconds then *
def minutes_to_milliseconds(m):
    return m*60*1000

#test
print("Test for question A:")
print("1 minute converts to", minutes_to_milliseconds(1), "milliseconds") #should return 60000 milliseconds
print("4.5 minutes converts to", minutes_to_milliseconds(4.5), "milliseconds") #should return 270000.0

#Function for question B
def average_of_two(a,b):
    return (a+b)/2

#test
print("Test for question B:")
first=int(input("Please enter first exam scores"))
second=int(input("Please enter second exam score"))
print("Average of ", first , "and", second, "is", average_of_two(first,second))

#Function for question C
def quadratic_equation(a,b,c):
    determinant = b**2 - (4*a*c)
    x1 = ((-1*b) + math.sqrt(determinant))/(2*a)
    x2 = ((-1*b) - math.sqrt(determinant))/(2*a)
    return x1,x2
#test
print("Test for question C:")
#def get_quadratic():
print("Please enter your quadratic equation in the form ax^2+bx+c")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
    #return a,b,c

#print("The roots are: ", quadratic_equation(get_quadratic()))
print("The roots are: ", quadratic_equation(a,b,c))

#Function for question D
def kevin_to_reaumur(k):
    return (k-273.15)*0.8

def reamur_to_celsius(r):
    return r*1.25

def kevin_to_celsius(k):
    return reamur_to_celsius(kevin_to_reaumur(k))

#test
print("Test for question D:")
print("60 Kelvin is ", kevin_to_reaumur(60), "Reaumur")
print(kevin_to_reaumur(60)," Reamur is ", reamur_to_celsius(kevin_to_reaumur(60)), "Celsius")
print("60 Kelvin is ", kevin_to_celsius(60), "Celsius")

#Function for question E -> box volume/sphere volume * packing density which is pi/3(sqrt(2))
def marbles_in_cube(n):
    #has to return as int
    return int(((n**3)/((4/3)*math.pi*((n/4)**3)))*(math.pi/(3*math.sqrt(2))))

#test
print("Test for question E:")
print(marbles_in_cube(100))


#Function for question F
def print_triangles():
    print("^ - ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")

def print_i():
    print("i        i        i        i        i")

def print_layer():
    print_triangles()
    print_i()
    print_i()
    print_i()
    print_i()

#test
print("Test for question F:")
print_layer()
print_layer()
print_layer()
print_layer()
print_triangles()
