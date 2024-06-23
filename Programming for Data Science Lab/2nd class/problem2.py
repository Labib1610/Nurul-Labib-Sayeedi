# a,b = 10,20
# a,b=b,a
# print(a,b )



# a,b = 10,20
# a,b=b,a
# print(a,b ,sep='\n')


# a=10
# b=20
# a=b          #a=20
# print(a)
# a=10
# b=a        #b=10
# print(b)




# a=x=10
# b=20
# a=b
# b=x
# print("a=",a,"b=",b)


'''a=10      multi line comment
b=20
x=a
a=b
b=x
print("a=",a)
print("b=",b)'''



# a,b,c,x=2,3,4,5
# equation=a*x**2+b*x+c
# print(equation)


# a,b,c,x=2,3,4,5
# equation=a*x**2+b*x+c
# str(equation)
# print("equation:"+str(equation))


# a,b,c,x=1,1,1,2
# equation=a*x**2+b*x+c
# print(equation)


# number1=input("Enter first integer: ")
# number2=input("Enter second integer: ")
# total=int(number1)+int(number2)
# print("The sum of",number1,"and",number2,"is",total)


# number1=input("Enter first integer: ")
# number2=input("Enter second integer: ")
# number3=input("Enter third integer: ")
# average=(int(number1)+int(number2)+int(number3))/3
# print("The average of",number1,number2,"and",number3,"is",average)

# """Data Type"""
# print(type(average))         #Data Type 
# message="hello"
# print(type(message))




'''problem'''
# number1=input("Enter first integer: ")
# number2=input("Enter second integer: ")
# number3=input("Enter third integer: ")
# average=int(number1+number2+number3)/3      """this line"""
# print("The average of",number1,number2,"and",number3,"is",average)


"""Conditional statement"""


# x=2
# print(x%2==0)

# x=int(input("Enter an integer: "))
# if x%2==0:
#     print("It is an even numebr!")
# else:
#     print("It is an odd number")
    
    
# x=int(input("Enter an integer: "))
# if x%2==0:
#     print("It is an even numebr!")
#     print("print inside if blocks")
# print("print outside of if blocks ")    



# x=int(input("Enter an integer: "))
# if x>10 and x%2==0:
#     print("x is an even number and it is greater than 10 ")
# else:
#     print("x is an odd number or it is less than or equal to 10 ")  





"""#nested condition"""         #Important

# x=int(input("Enter an integer: "))
# if x>10 and x%2==0:
#     print("x is an even number and it is greater than 10 ")
# else:
#     if(x<=10):                                    
#         print("x is an odd number or it is less than or equal to 10 ")
#     else:
#         print("The number is greater than 10")    
        
        
# x=int(input("Enter an integer: "))
# if(x==1):
#     print("x=1")
# elif(x==2):
#     print('x=2')
# elif(x==3):
#     print('x=3')
# else:
#     print('The number is not between 1-3')


# x=int(input("Enter an integer: "))
# if(x==1):
#     print("x=1")
# elif(x==2):
#     print('x=2')
# elif(x==3):
#     print('x=3')



# grade=int(input('The number on the subject'))
# if(grade>=90 and grade==100):
#     print("Your grade is A")
# elif(grade>=86 and grade<=89):
#     print("Your grade is A-")
# elif(grade>=82 and grade<=85):
#     print("your grade is B+")
    
    
    
# grade=int(input('The number on the subject: '))
# if(100==grade>=90 ):
#     print("Your grade is A")
# elif(grade>=86 and grade<=89):
#     print("Your grade is A-")
# elif(grade>=82 and grade<=85):
#     print("your grade is B+")
# else:
#     print("Other grade!")