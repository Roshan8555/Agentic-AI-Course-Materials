'''
def fname():
    name = 'codegnan'
    return name
print(fname())

count = 15
def update():
    global count
    count = count + 10
    return count
print(update())
print(f'update value of count is {count}')

def outer():
    count = 10
    def inner():
        nonlocal count
        count = count + 5
        return count
    print(inner())
    return count
print(outer())

len = 34
print(len)

def update(numbers):
    number = 15
    number = number + 5
    return number

print(update(5))
number = 23
print(update(number))
print(number)
print(update('3'))

def update(numbers):
    return number * 3
print(update(3))
print(update(25))
print(update(number))

def update(numbers):
    return numbers * 2  #here numbers * 2 repeats the list twice.
print(update([1, 2, 3])) 
print(update([4, 5]))

#Pass by Object Reference in Python.
#Mutable objects (like lists, dictionaries, sets) can be modified inside the function.
#Immutable objects (like integers, strings, tuples) cannot be modified in place.

def update(numbers):
    numbers.append(100)
    return numbers
print(update([1,22,3]))
print(update([0,50]))

def update(numbers):
    numbers.append("roshan")
    return numbers
print(update([1,2,3]))

def update(numbers):
    my_list = [1,2,3,'ff']
    return my_list
print(update([2,4]))

#functions are termed as first class objects-->
#function inside another funstion --> enclosing scope (nonlocal)
#function can be used as an argument to another function --> list(map(int,input()))
#function can call itself (Recursive Functions)
#Function can return Another function

#built-in-functions --> python by default has built-in-functions which makes the logic easier.

if __name__ == '__main__':
    print(2+34)
    print(dir())
    print(dir(__builtins__))

data = ['rosh','sai','sam']
print(all(data))
data.clear()
print(all(data))
d = [None,23,24]
print(all(data))
print(bin(6)) #returns binary representation of an object.
print(chr(63)) #input any integer --> returns sepecific character.
print(bool(0)) #output Boolean (True/False)
print(complex()) #returns complex number
print(dict(name = "roshan",place = "hyd")) #returns a dictionary

print(divmod(5,3)) #returns the divison module in a tuple.
#enumerate() , eval()

details = ['codgnan','roshan','AAI']
print(dict(enumerate(details)))
print(dict(enumerate(details,1)))

details = ['codgnan','roshan','AAI']
for i in details:
    print(details.index(i),":",i)

a = eval(input("enter a dictionary:")
print(a)
print(id(a))
b = [23,1,4,6]
print(tuple(sorted(b)) #sorted () by default returns list
print(min(b))
print(max(b))

#factorial of N

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("enter a value: "))
print(factorial(n))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative number"
    else:
        return n * factorial(n - 1)
n = int(input("enter a value: "))
print(factorial(n))

#find the sum of natural numbers till 10 using recersive function.

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
n = int(input("enter a value: "))
print(sum(n))

#create a function to return the area of rectangle

def area_of_rectangle(length,breadth):
    if length == 0 or breadth == 0:
        return 0
    else:
        return length * breadth
length = int(input("enter a value of length: "))
breadth = int(input("enter a value of breadth: "))
print(area_of_rectangle(length,breadth))

#syntax: --> var_name = lambda parameters : expression
b = lambda l,b : l+b
print(type(b))
print(b(5,6))

#find the area of square using lambda
c = lambda side : side * side
side = int(input("enter the measurements: "))
print(c(side))

#user registration in a webpage -->
#first name --> input
#last name --> input
#full name

#write user defined them anonymous function

# User Registration using User-Defined Function

def full_name(first_name, last_name):
    return first_name + " " + last_name

first = input("Enter First Name: ")
last = input("Enter Last Name: ")

name = full_name(first, last)

print("Full Name:", name)

#to get even number from user
n = int(input("enter a value: "))
result = lambda n : n if n%2 == 0 else "Odd"
print(result(n))

#length of sequences
name = input("enter the message: ")
result = lambda name : len(name)
print(result(name))

#filter(), map()

#list of intgers
a=list(map(int,input("enter the values:").split(',')))
print(a)
#filter only even numbers
b = list(filter(lambda x:x%2==0,a))
print(b)
names=['pavan','abhi','roshan','madhu','roshan','vasanthi']
final_names=list(filter(

#map() --> it will apply for every value from multiple iterations
a = list(map(int,input("enter the values: ").split(',')))
print(a)

names = ['codegnan','roshan','hyd']
result = list(map(lambda name:name.upper(),names))
print(result)

prices = [1000,2500,3500,4000]
final_price = list(map(lambda price: (price - price * 0.1),prices))
print(final_price)
'''
#reduce() --> this makes complete iterable to be a single value --> functools
from functools import reduce
numbers = [1,2,3,4,5]
result = reduce(lambda a,b:a+b,numbers)
print(result)


































           

