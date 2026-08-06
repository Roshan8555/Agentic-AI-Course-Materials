'''
in this usecase (mini_project),we will make use of control block statements
#bmi -- > body mass index --> bmi = (weight(kg)) / (height**2) (meters)

#weight = 70
weight = int(input("Enter the weight in kgs: "))
height = float(input("enter the height in meters : "))
#print(bmi)
#we want to make it dynamic and build BMI calculator
#(<18.5 --> underweight,18.5 - 24.9 --> normal weight ,25 - 29.9 --> overweight >=30 obesity)
if weight > 0 and height > 0:
    bmi = (weight) / ((height**2))
    if bmi < 18.5:
        print(f'you are underweight as bmi is {bmi}')
    elif 18.5<=bmi<24.9:
        print(f'you are in perfect shape,bmi is {bmi}')
    elif 25<=bmi<29.9:
       print(f'you are overweight need to maintain diet , bmi is {bmi}')
    elif bmi>=30:
       print(f'obesity,your bmi is {bmi}')
else:
    print(f'enter only +ve values')

#task --> for same above BMI calculator store the details in a dictionary
#o/p --> BMI results = ( 'name':(user1,user2,user3),
    #                     'BMi_values':(BMI1,BMI2,BMI3)

while True:
    try:
        weight = int(input("enter the weight in kgs: "))
        height = float(input("enter the height in meters: "))
        if weight > 0 and height > 0:
            print(f'valid input received')
        else:
            print(f'make sure to enter only +ve values')
    except ValueError:
        print("make sure to enter only valid input")
'''
#syntax --> user defined fumctions
def add(a,b):
    c = a + b
    print(f'value of c is {c}')
#add('code','gnan')
print(add(12,3,45),(4,3,5))
print(add('code','gnan'))
result = add('code','gnan',23)
print(result)
    
