#Wilson Song
#afternoon1
#@23466407

import math


#question1:
print("Question 1.")
def perfect_number(x):
    sum=0
    for counter in range(1,x):
        if x%counter==0:
            sum=sum+counter
    if sum==x:
        return True
    else:
        return False

moredata="yes"
while moredata[0]=="y":
    try:
        user_input=int(input("Please enter a positive integer>>"))
    except ValueError:
        print('Please only enter a positive integer!! Try again!!')
    except:
        print("Something went wrong")
    if perfect_number(user_input):
        print(user_input, " is a perfect number! ")
    else:
        print(user_input, " is not a perfect number!")
    moredata=input("Would you like to continue? Yes or No ")

print("Question 1 Done.")
print("---------------------------------------------------------")
#question 2
print("Question 2.")
def isDivisor(n,x):
    if n%x==0:
        return True
    else:
        return False

moredata2="yes"
while moredata2[0]=="y":
    user_input=int(input("Please enter a positive integer>>"))
    counter=1;
    while counter<=user_input:
        if isDivisor(user_input,counter):
            print(counter)

        counter=counter+1
    moredata2=input("Would you like to continue? Yes or No ")
print("Question 2. Done.")
print("---------------------------------------------------------")

#question3
print("Question 3.")
moredata3="y"
while moredata3[0]=="y":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))  

    first_side = ((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2))
    second_side = ((((x2 - x3) ** 2) + ((y2 - y3) ** 2)) ** (1 / 2))
    third_side = ((((x3 - x1) ** 2) + ((y3 - y1) ** 2)) ** (1 / 2))

    if first_side + second_side > third_side and first_side + third_side > second_side and third_side + second_side > first_side:
        print("The coordinates create a triangle.")
    else:
        print("The coordinates do not create a triangle.")

    moredata3=input("Would you like to continue? Yes or No ")
print("Question 3. Done.s")
print("---------------------------------------------------------")

#Question4
print("Question 4.")
def isPrime(x,counter): #function used to determine whether a number is prime
    if counter >= x:#base case for when the counter rises above the number to return
        print(x)
        return
    if x == 2: #special case where 2 is always a prime
        return True
        print(x)
        return
    elif x % counter == 0: #if it is divisible then it is not a prime
        return False
        return isPrime(x, counter + 1) #recurse
    else:
        return True
        print(x)

moredata4="yes"
while moredata4[0]=="y":
    init=int(input("Please enter the initial integer>>"))
    fin=int(input("Please enter the final integer>>"))
    counter=init
    print("The prime numbers between ", init, "and ", fin, "are:")
    while counter<=fin:
        if isPrime(counter,2):
            print(counter)

        counter=counter+1
    moredata4=input("Would you like to continue? Yes or No ")

print("Question 4. Done.")
print("---------------------------------------------------------")

#question5
print("Question 5.")
moredata5="yes"
while moredata5[0]=="y":
    x_people = int(input("Please enter the number of people - X:"))
    y_seats = int(input("Please enter the number of seats - Y:"))

    print("The number of ways is ",float((math.factorial(x_people)/math.factorial(y_seats))))

    moredata5=input("Would you like to continue? Yes or No ")

print("Question 5. Done.")
print("---------------------------------------------------------")


