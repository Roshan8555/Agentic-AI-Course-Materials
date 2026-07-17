Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:00:00) [MSC v.1938 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sequence datatypes (set,tuple,list),none
#list -> Mutable, Ordered, Indexed and heterogenous collection -> []
#type conversion of int,float,complex,bool --> list
age = 25
type(age)
<class 'int'>
b = list(age)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b = list(age)
TypeError: 'int' object is not iterable
c = list((1,2))
print(c)
[1, 2]
print(age)
25
age = 25
b = list((rosh,5,6,3))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b = list((rosh,5,6,3))
NameError: name 'rosh' is not defined
b = list((3,6,7))
print(c)
[1, 2]
print(b)
[3, 6, 7]
c
[1, 2]
size = 2.5
b = int(size)
b
2
c = list(size)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    c = list(size)
TypeError: 'float' object is not iterable
a = "Hello,world"
print([2,4])
[2, 4]
print(a([2,4]))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(a([2,4]))
TypeError: 'str' object is not callable
size = 2.6
tuple(size)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(size)
TypeError: 'float' object is not iterable
tuple = (20,30,40)
size(tuple)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    size(tuple)
TypeError: 'float' object is not callable
tuple = ((20,30,40))
size(tuple)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    size(tuple)
TypeError: 'float' object is not callable
tuple = [20,30,40]
size(tuple)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    size(tuple)
TypeError: 'float' object is not callable
tuple = (20,30,40)
len(tuple)
3
print(numbers)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(numbers)
NameError: name 'numbers' is not defined
print(type(tuple))
<class 'tuple'>
value = 45
b = str(value)
b
'45'
print(b)
45
type(b)
<class 'str'>
type(value)
<class 'int'>
size = 1.5
b = str(size)
b
'1.5'
print(b)
1.5
type(b)
<class 'str'>
c = 3+4j
type(c)
<class 'complex'>
c
(3+4j)
d = str(c)
print(d)
(3+4j)
e = str(true)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    e = str(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
e = str(True)
e
'True'
print(e)
True
age = 20
b = set(age)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    b = set(age)
TypeError: 'int' object is not iterable
age = 20
b = set(1.3)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b = set(1.3)
TypeError: 'float' object is not iterable
b = set(1,2)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    b = set(1,2)
TypeError: set expected at most 1 argument, got 2
b = set(1)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b = set(1)
TypeError: 'int' object is not iterable
b = set((1,2))
b
{1, 2}
print(b)
{1, 2}
len(b)
2
a = 50
b = dict(a)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    b = dict(a)
TypeError: 'int' object is not iterable
b = dict(2)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    b = dict(2)
TypeError: 'int' object is not iterable
b = dict((2))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    b = dict((2))
TypeError: 'int' object is not iterable
b = dict({2})
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    b = dict({2})
TypeError: cannot convert dictionary update sequence element #0 to a sequence
a = (2,3,5,6)
len(a)
4
b = [2,2,4,6]
b
[2, 2, 4, 6]
print(b)
[2, 2, 4, 6]
c = {2,2,1}
c
{1, 2}
d = [rosh,2,1,2]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    d = [rosh,2,1,2]
NameError: name 'rosh' is not defined
>>> d = [ "rosh",2,1,1]
>>> d
['rosh', 2, 1, 1]
>>> e = ("rosh",2,2)
>>> e
('rosh', 2, 2)
>>> type(e)
<class 'tuple'>
>>> print(e[1,2])
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(e[1,2])
TypeError: tuple indices must be integers or slices, not tuple
>>> print(e([1,2]))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(e([1,2]))
TypeError: 'tuple' object is not callable
>>> print[e[1,2]]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print[e[1,2]]
TypeError: tuple indices must be integers or slices, not tuple
>>> a = 2
>>> b = 3
>>> c = a - b
>>> c
-1
>>> print(c)
-1
>>> d = a * b
>>> d
6
>>> e = a \ b
SyntaxError: unexpected character after line continuation character
>>> e = a \ b
SyntaxError: unexpected character after line continuation character
>>> e = a / b
>>> e
0.6666666666666666
>>> r = a // b
>>> r
0
