#patterns in python
'''
n = int(input("enter a value:"))
for i in range(1,n+1):
    for j in range (1,n+1):
        #print(i,j)
        if j <= n-i:
            #print(i,j)
            print(" ",end="")
        else:
            print('*',end=" ")
    print()

def grocery(**items):
    print(items)

    for key,value in items.items():
        print(f'key is {key}')
        print(f'Value is {value}')
grocery()
grocery(name='MILK',price=35,quantity='1000ml',brand='heritage')

def bmi_calc(*kwargs):
    while True :
        try:
           if weight > 0  and height > 0 :
            break 
           else:
            print(f'make sure to enter only +ve values,no negative values')
        except ValueError:
            print('invalid input only integer for weight/int , float for height ,enter properly')
    bmi = (weight) / ((height**2))
    if bmi < 18.5:
        print(f'{name}you are underweight as bmi is {bmi}')
    elif 18.5<=bmi<24.9:
        print(f'{name}you are in perfect shape,bmi is {bmi}')
    elif 25<=bmi<29.9:
        print(f'{name}you are overweight need to maintain diet , bmi is {bmi}')
    elif bmi>=30:
        print(f'{name}obesity,your bmi is {bmi}')
                
weight = int(input("enter the weight "))
height = float(input("enter the height in meters:"))
bmi_calc(weight,height)


