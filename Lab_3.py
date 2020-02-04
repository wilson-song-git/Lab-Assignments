#Wilson Song
#afternoon1
#23466507



#question 1
print("Question 1: ")
def collatz_conjecture(x):
    if x==0:
        print(x)
    elif x<0:
        print("Error: Input was negative")
    else:
        if x==1:
            print(x)
            return x;
        if x % 2 == 0:
            print(x)
            return collatz_conjecture(x/2)
        else:
            print(x)
            return collatz_conjecture(3*x+1)


try:
    x=int(input(('Please enter a value for n')))

except ValueError:
    print('please enter an integer:')

except RunTimeError as excObj:
    if str(excObj)== "maximum recursion depth exceeded":
        print("please enter a positive integer")
except:
    print("Something went wrong")


collatz_conjecture(x)


#question 2
print("Question 2:")
try:
    a=float(input("Enter a number: "))
    b=float(input("Enter a number: "))
    c=float(a/b) #used to try the division
except ValueError:
    print("Please only enter numbers")
except ZeroDivisionError:
    print("The second integer cannot be 0")
except:
    print("Something went wrong")

print(float(a/b))

#question 3:
print("Question 3:")
def print_prime_factors(x,factor):

    if x < factor:
        return
    if x % factor==0:
        print(factor)
        return print_prime_factors(x/factor,2)
    else:
        return print_prime_factors(x,factor+1)
try:
    n=int(input("Enter a number you would like to be factored: "))

except ValueError:
    print("Error:Input was not an integer")
except:
    print("Something went wrong")

print_prime_factors(n,2)

#Question 4
print("Question 4: ")
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
m
def print_prime(x):
    if x<=1:
        return
    if isPrime(x,2):
        print(x)
        return print_prime(x-1)
    else:
        return print_prime(x-1)
try:
    z=int(input("Please enter a number:"))
except ValueError:
    print("Enter a integer only.")
except:
    print("Something went wrong")
print_prime(z)