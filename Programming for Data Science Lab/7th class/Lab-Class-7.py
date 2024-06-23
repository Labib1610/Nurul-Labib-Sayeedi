def greetings(name='Unknown'):          # default value
    print('Hello',name)


def sum(a,b):
    sum = a+b
    return sum


def add():
    a=int(input('Enter the first integer: '))
    b=int(input('Enter the second integer: '))
    sum = a+b
    print('Inside add function: ',sum)


def keyValue(city,country):
    print('I live in ', city)
    print('My country name is ',country)

def funcList():
    myList = []
    for i in range(5):
        myList.append(i)
    return myList

name = input('Enter your name: ')
a=5
b=10
greetings()
greetings(name)
result = sum(a,b)
print('Total Sum: ',result)
add()
keyValue(city='Dhaka',country='Bangladesh')
x = funcList()
print(x)  