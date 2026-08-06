'''
#str -->list,tuple,dict
name = 'codegnan'
print(type(name))
g = list(name)
print(g)
h = name.split()
print(h)
j = name.split(",")
print(j)
e = dict.fromkeys(name)
print(e)

#input formating --> list input,tuple input,dict input, -->eval()
#list as input
data = eval(input("enter the list:"))
print(data)
print(type(data))
data = eval(input("enter the tuple values:"))
print(data)
print(type(data))

details = eval(input("enter the student detils:"))
print(details)
print(type(details))

#repetition statements (loops) -->for, while
#loops will automate the tasts

#for loops is used to iterate the items in a collection (str,tuple,lits..) also can generate a sequence of numbers (range)

syntax for :

for <loop_var> in collection/range_function:
    statement(s)...
    .....
....
marks = [24,25,21,20]
for mark in marks:
    print(mark)
    print(mark,end='\t')

#find the sum and average of marks
marks = list(map(int,input("enter the marks:").split(",")))
print(marks)
total = 0; avg = 0
for i in marks:
    total = total + i
    #print(total)
    #avg = sum / len(marks)
    #print(avg)
print(f' sum of the given marks is {total}')
print(f' avg of the given marks is {total/len(marks)}')

#[1,3,4,5,'codegnan',3,'agents',2,4]
#find the sum of the above list

data = [(1,3,4,5),'codegnan',3,'agents',2,4]
print(type(data))
print(data[0])
print(data[3])
total = 0
for i in data:
    if type(i) in (int,float):
        total += i
    print(total)
print(f'sum is {total}')

details = {'names':['sai','abhi','ram'],
           'marks':[24,20,28]}
print(details.items())
''' #for i in details:
    #print(i)
'''
for key in details:
    print(key)
for value in details.values():
    print(value)

for key,value in details.items():
    print(f'key is {key}')
    print(f'value is {value}')

#range (start,end,stop) --> generate the sequence of values
#range(end) #by default start is 0

for i in range(5):
    print(i)
    print(f'value of 1 is {i}')
#range(start,end)
for i in range(1,22):
    print(i,end = ' ')
#range of (start,end,stop)
for i in range(1,22,3):
    print(i)'''
#in same way return numbers in reverse order
for i in range(10,-1,-1):
    print(i,end = ' ')
for i in range(ord("A"),ord("Z"),+ 1):
    print(chr(i))
#daily workout log ==> fitness streak
work_log = [1,1,1,0,1,1,0]
longest_streak = 0
current_streak = 0
for day in work_log:
    #print(day)
    if day == 1:
        current_streak += 1
    elif current_streak > longest_streak:
        longest_streak = current_streak 
