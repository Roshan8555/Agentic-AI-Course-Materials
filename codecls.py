'''
age  = 24
if age > 18:
    print("True")
else:
    print("False")

#membership operators --> in,not in -->returns boolean
#they check for the existance of an object in a collection
#list[]

friuts = ["apple,banana,mango"]
print(friuts)

        
books = {"physis","maths","hindi","maths"}
print(books)

marks = 74
if marks > 35:
    print("Pass")
else:
    print("Fail")

marks = "absent"
if marks == "absent":
    print("absent")
elif marks > 35:
    print("Pass")
else:
    print("Pass")

number = 7
if number + 6 ==0:
    print("True")
else:
    print("False")

number = 8
if number == 0:
    print("Zero")
elif number > 0:
    print("Positive")
else:
    print("Negative")


#input formatting --> input()

#string input -->name,emailids,username...

name = input()
print(name)

#print(name)
name = input("enter the name:")
print(name)
print(type(name))

#integer input
age = int(input("enter the age:"))
print(age)
print(type(age))

#float input
size = float(input("enter the size:"))
print(size)
print(type(size))
'''
'''
#complex input
num = complex(input("Enter the number:"))
print(num)
print(type(num))

cost_price = int(input("enter the cost price:"))
selling_price = float(input("enter the selling price:"))
loss =cost_price - selling_price
print(loss)


#multiple string inputs
name,place = input("enter the details:").split() # to seperate the details we are using split() the space in the understand the its need to split the value when we use space in the input
print(name)
print(place)

name,place = input("enter the details:").split(',') #here instead of space we are using comma(,) symbol to seperate the detalis 
print(name)
print(place)

name,place = input("enter the details:").split(".")
print(name)
print(place)

#multiple integer values
#(So, map() is not for printing—it's for converting data into the type you need. In this case, it converts strings to integers so you can perform arithmetic operations.)
a,b = map(int,input("Enter the numbers:").split(","))
print(a)
print(b)

#multiple float values
a,b = map(float,input("Enter the numbers:").split(","))
print(a)
print(b)


#list of strings
data = input("enter the values:").split(",")
print(data)

#list of integers
marks = list(map(int,input("Enter the values:").split(",")))
print(marks)

#list of float values
sizes = list(map(float,input("Enter the values:").split(",")))
print(sizes)

#output formatting
#print()
print(34)
print(23,21,'rosh')

#separator --> for seperating ths values
print(23,32,44)
print(23,21,566,sep=',')
print(23,23,22,sep='\n')

#end argument in print() ==> \n --> new line
print(56,657,'yyf',end='\t') #\t -->tab space

#using commas
name = 'codegnan'
place = 'hyd'
print(name,place)
print("Name :",name,"Place :",place)

#old style formatting --> %d,%S,%f
age = 32;place = 'hyd'
print("Age is %d and place is %s"%(age,place))
price = 456.96
print("Price is %f"%(price))

#using str().foramt() method
name,course = 'roshan','python'
print("{} is enrooled in {} course".format(name,course))

#f-string notation ---> most recommended
name,course = 'roshan','python'
print(f'{name} is enrolled in {course}')
print(f'{"codegnan"}')

#sequence data types --> Strings --> group of characters enclosed in single,double or triple qoutes
#strings are immutable, ordered and indexed collection

name ='roshan'
name ="roshan"
name ='roshan'
#to access the number of objects in a collection --> len()
print(name)
print(len(name))
#to access the type of string --> type()
print(type(name))
print(type(input()))

roll_no = 'BU22CSEN0400171' #alphanumeric string
print(roll_no)

moblie_no = '3456789876543'
print(moblie_no)

#operations on Strings --> Repetition,concatenation, Indexing,Slicing,Membership..

#concatenation (merging) --> combine multiple strings (+)
name = 'roshan';place = 'hyd';collage = 'gitam';
print(name + place + collage)
print(f'{name} is from {place} where he studied from {collage}')

#repetition --> we use * operator
data = 'roshan'
print(data*3)
print('roshan' * 20)

#membership --> in,not in
print('code' in 'codegnan')
print('roshan' not in 'codegnan')

#slicing in strings
#indexing --> we can acces the position of an object in a string, we can use [] to get the index of an object
#it starts with 0 and ends with len(obj) - 1
#slicing --> accessing group of characters --> start node include and end node is excluded.
name = 'roshan'
print(name[2:5])
name = 'rosh'
print(name[0:3])
name = 'i am roshan'
print(len(name))
print(name[5:8])
name = 'agentic ai course'
print(len(name))
print(name[-5])
#strings are immutable and item assignment not possible.
name = 'roshan'
print(name[:])
print(name[:3])
print(name[2:])
print(name[2:-3])
print(name[2:23])
name = 'codegnan'
print(name[-5:-1])

name = 'roshan'
print(name[2:-2])

#[::]--> [start:end:stop]
name = 'codegnan'
print(name)
b = name[::]
print(b)
print(b[::1])# it also prints the complete string
print(b[::4])
print(b[2:9:5])
print(b[:4:5])

print(name[::-1]) #prints in reverse order
print(name[::-2])
print(name[::-6])

print(name[-0:-1:])#returns complete excluding last character
print(name[-0:-1:-2])#returns empty string as no possibilities
print(name[-0:-1:2])

#built-in functions --> len(), min(), max(), ord(), char()
place = 'Hyderabad'
print(place)
print(len(place))
print(min(place)) #returns "H" as per ASCII values
print(max(place))
print(ord('A')) # returns ASCII value of given character
print(chr(97)) # returns the specific character as per the ASCII values

course = "Agentic AI"
print(course)
print(course.lower())
print(course.upper())
print(course.swapcase())
print(course.title()) #first letter of every word will be capitalized
print(course.capitalized()) #first letter will be capaitalized

print(sorted("roshan"))

#sequence Types --> lists --> mutable,indexed,ordered and heterogenous collection.
#Nested lists --> List inside another lists

data = ['codegnan',35,4.56,['python','java','AI','DA'],100,45]
print(data)
print(len(data))
print(data[3]) # we need to acces the inner list
#now i want to get 'python' and 'java' from the above list
print(data[3][:2])
print(data[3][2:])
#get only 'pyt'
print(data[3][0][:3])
print(data[3][1][1:])
print(data[3][0][2:4])
#get the output as ['python','data']
print(data[3][0::2])
#get the output as [35,['python','java','AI','DA']45]
print(data[1::2])

#lists are mutable --> we can insert/remove elements
data = ['codegnan',35,4.56,['python','java','AI','DA'],100,45]
#using indexing and slicing -->change
#35-->45
data[1] = 45
print(data)
print(len(data))
data[3] = ['python','Rag','AI','DA']
print(data)
data[3][1] ='rag'
print(data)
#indexing will never change the length of the collection
#now we will use "slicing"
data[1:3] = ['Roshan','kumar']
print(data)
data[2:5] = ['venky','sai']
print(data)
data = ['codegnan',35,4.56,['python','java','AI','DA'],100,45]
data[3][1::2] = ['Rag','Mcp']
print(data)
#indexing,slicing,striding can insert elements but we loose our original data

#append(),extend(),insert()
#append()--> inserts only single object at the end of the list/empty list we can start assign

details = ['Roshan',32,'codegnan']
print(len(details)) #append will increse the len()
details.append(34)
print(details)
details.append(data)
print(details.append('roshan')) #it returns None as we need to print only list

age = []
age.append(1)
age.append(2)
print(age)
#extend --> insert multiple objects(iterable) in the end of the list
#details.extend(34,32)
#print(details) #typeError
details = ['Roshan',32,'codegnan']
details.extend((32,54))
print(details)
details.extend('roshan') #it splits everey character
print(details)

details.extend(['roshan'])
print(details)
#insert() --> inserts objects before the index
details.insert(1,'python')
print(details)
print(len(details))
details.insert(3,['ugyf','dgcgv'])
print(details)
details.insert(20,'vishnu')
print(details)
details[-1].append('khaja')
print(details)

#pop(),remove(),clear()
#pop() removes by default last index if not given
details = ['Roshan',32,'codegnan']
details.pop()
print(details)
details.remove(32) #removes the first occurance of a value
print(details)

#index(),count(),copy(),sort(),reverse()
details = ['Roshan',32,'codegnan','Roshan']
print(details.count('Roshan'))
print(details.index('Roshan'))
print(details.('Roshan'))

#tuples --> tuples are immutable,ordered, heterogenous
#indexed sequence type, we use () for declaration
data = 1,23,2
print(data)
print(type(data))

#nested tuples and also have lists inside it.
details = ('codegnan',32,(2,4,5),'roshan',[12,45,'agents','rag'])
print(details)
print(len(details))
print(details[2])
print(details[4][2])
print(details[0])
details[0] = details[0].replace('n','f') #tuples are immutable we cannot modify it.
print(details)

details = ('codegnan',32,(2,4,5),'roshan',[12,45,'agents','rag'])
details[4][2] = details[4][2].replace('a','A') #here we are using lists so its mutable
print(details)
print(details[1:4])
print(details[::3])
print(details[2::5])
print(details[3::])
#practice yourself indexing, slicing and striding
print(type(details[4])) #always use type()
details[4].remove('agents')
print(details)

#operations on tuples --> indexing slicing,membership,concatenation/merging,repetion
age = 22,21,25,32
ids= 231,232,213
print(age+ids)
print(age*2)
#len(),type(),min(),max(),sorted()
age=(25,12,45,65)
print(min(age))
print(max(age))
print(tuple(sorted(age)))
#indexing(),count()
details = ('saketh','codegnan','agentic ai',35,25,25)
print(details)
print(details.index(35))
print(details.count(35))
#convert string to list/tuple

data='AgenticAi'
print(type(data))
data=list(data)
print(data)

#set datatype-->sets,frozen sets
#sets-->A set is a unique,mutable collection-->set(),unordered
a={}
b=set()
print (type(a))
print (type(b))

ids={252,254,155,145,145,155,185}
print(ids)
print (len(ids))

#data ={23,4.5,'codegnan',{12,34,5}}
#print (data)

ids={252,254,155,145,145,155,185}
ids.add(156)
print(ids)
#ids.add(ids)
#print(ids)
ids.update(['saketh'])
print(ids)
details= ['siva','mani','roshan']
ids.update(details)
print(ids)

#remove elements from a set-->discard(),remove(),clear(),pop()
ids={252,254,155,145,145,155,185}
ids.discard(145)
print (ids)

#ids.remove(123)#retuns key error
#print(ids.discard(123))#discard will avoid error

print(ids.pop())#remove and returns arbitary elements from a set
print(ids.pop())
print(ids.pop())

#union,intersection,difference,symmetric Difference,subsets,supersets
ages={35,23,25,45,32}
print(ages)
d = ids.union(ages)
print(d)
e = ids.update(ages)
print(e) #here it returns None as update is happening in ids set.
print(ids)

f = ids.intersection(ages)
print(f)

g = ids.intersection_update(ages)
print(g)
print(ids) #picks common elements from both sets and updates the first set

h = ids.difference(ages)
print(h) #remove common elements and return remaining elements in the first set

#  |(union), &(intetsection) , - (difference), ^(symmentric difference)
g = ages - ids
print(g)
u = ids | ages
print(u)
f = ids ^ ages
print(f)
j = ages.symmetric_difference(ids)
print(j)

a = {1,2,3}
b = {1,2,3,4,5}
#below functions will return boolean
print(a.issubset(b)) #all elements of a set are present in set b
print(b.issuperset(a))
print(a.isdisjoint(b)) #it returns false as set a is already a subset of set b

#Frozenset --> immutable set
data = frozenset(ids)
print(data)
print(type(data))

#we cannot insert/remove elements but mathmatical operations are possible
temp_details = frozenset([34,35,34,32,31])
print(temp_details)
print(min(temp_details))
print(max(temp_details))
print(sorted(temp_details))

#hometask pratice lists and sets create a nested sequence include a list with tuples and sets and strings

nested_sequence = ["Python",("Java","c"),{"Roshan","Venky"},["codegnan",("hyd","AI"),{"data","machine learning"}]]
                   
print(nested_sequence)

#dictionary --> Collection of key-value pairs,mutable,unOrdered.. --> {},dict()

details = {}
print(details)
print(type(details))

details = {"Name":"Codegnan","place":"Hyd","age":7}
print(details)
print(len(details))

#accessing Keys
print(details['Name'])
print(details['age'])
#keys must be unique in a dictionary
data = {'Age':23,'name':"roshan",'Age':22}
print(data) #here the output we get is age is 22 only because it will data the recent update value only for duplicates 
#in dictionary "we do index by using keys".
'''
#create dictionaries using other datatypes
students_data = {'ids':[23,23,45,43],
                 'names':['roshan','surya','sai','venky'],
                 'place':['blr','chennai','kadapa','hyd'],
                 'gender':['male','male','male','male']}
print(len(students_data))
print(students_data.keys()) #returns Keys from dictionary
print(students_data['names'])
print(students_data.values())

#updating dicyionary
students_data['Course'] = {'PFS',"JFS","AAA"}
print(students_data)
print(type(students_data))

print(type(students_data['ids']))
#now if we want to insert 3 more unique ids
#students_data['ids'] = 56,54,32 #this is not recommoned in this case

#print(students_data)
students_data['ids'].extend([56,54,32])
print(students_data)

students_data['names'].insert(1,'ashok')
print(students_data['names'])
###we want to insert new place
students_data['place'] = list(students_data['place'])
print(students_data['place'])
####students_data.append['vizag'])
students_data['place'].append('vizag')
print(students_data['place'])
#print the below outputs
#['JFS','DA'] do in a single step
#[23,45,56,54,32] your ids should be as shown.
students_data['Course'] = ['PFS', 'JFS', 'AAA', 'DA']
print(students_data['Course'][1::2])
print(students_data['ids'][0:1] + students_data['ids'][2::2] + students_data['ids'][5:])

#keys(),values(),items()
print(students_data.items()) #returns key value pairs as tuple

#get will return value if key is existing, else default --> None
print(students_data)
print(students_data.get('names'))
#print(students_data['branch']) #returns key error because we not have branch.
#setdefault() --> update the dictionary if key is not existing with default none

print(students_data.setdefault('ids'))
#students_data.setdefault('branch')
students_data.setdefault('branch',['cse','ece','IT'])
print(students_data)

#update(),#ppop,popitem(),clear()
students_data.update({'fees':[34567],'marks':[32,32,76]})
print(students_data)
students_data.pop('marks') #we need to mention the key which we wnated to remove
print(students_data)
students_data.popitem() #comes from the lasr
print(students_data)
#clear() and copy() work it and..

#fromkeys() will create a new dictionary by accepting each object in the given iterable as
#key whereas value is set to None
ids = [23,45,56]
#to convert above list to dictionary
d = dict.
fromkeys(ids) #each value will be assigned as None we can modify accordingly
print(d)
d[23] = 'random'
print(d)

#print(d + d) #not possible for sets and dicts
#membership --> in,not in (keys)
print(23 not in d) #returns True as we have 23 as a key

#nested dictionary

data {
    's1':('id':23,
          'name':'ram',
          'place':'hyd'},
    's2':('id':25,
          'name':'sony',
          'place':'blr'}}
print(data.keys())





























