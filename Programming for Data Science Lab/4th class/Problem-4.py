# number_list  =  [1,2,3,4,5]

# mix_list  = [1,1.5,'a']             #different type variable

# print(len(number_list))                 #list item number

# list_len = len(number_list)
# print(list_len)

# print(number_list[0],number_list[4])

# number_list[0]=0            #exchange


#append()

# list  =  []
# list.append('honda')
# list.append('suzuki')
# list.append('yamaha')
# list.append('suzuki')    #list allow duplicate value
# print(list)


# list  =  ['yamaha','suzuki']
# list.insert(0,'ducati')
# print(list)



# list  =  ['yamaha','suzuki']
# del list[1]
# print(list)


# list  =  ['yamaha','suzuki']
# popped_list = list.pop()            # we use pop() to see the removed item
# print(popped_list)

# list  =  ['yamaha','suzuki']
# list.remove('yamaha')
# list.remove('X')          #Value error
# print(list)


# list  =  ['yamaha','suzuki','yamaha']
# list.remove('yamaha')

# my_list = ['Sunday',1.5,'A',10,10]

# #a)Ans.

# my_list.append('A')
# print(my_list)

# #b)Ans.
# # my_list = ['Sunday',1.5,'A',10,10]

# my_list.pop()                #del my_list[-1]
# print(my_list)

# #c)Ans.
# # my_list = ['Sunday',1.5,'A',10,10]

# removed_second = my_list.pop(2)
# print(my_list)
# print(removed_second)

# #d)Ans.
# # my_list = ['Sunday',1.5,'A',10,10]

# del my_list[1]
# print(my_list)

# #e)Ans.
# # my_list = ['Sunday',1.5,'A',10,10]

# my_list.append("Hello")
# print(my_list)

# #f)Ans.
# # my_list = ['Sunday',1.5,'A',10,10]

# print(len(my_list)) 


# my_list = [1,2,3,4,5]
# print(my_list[2:4])

# my_list = [1,2,3,4,5,6,7,8,9,10]
# print(my_list[5:9])


'''Important'''

# my_list = [1,2,3,4,5,]
# print(my_list[:4])
# print(my_list[:-1])
# print(my_list[0:])
# print(my_list[3:])


'''For Loop'''

# for i in range(10):
#     print('Hello')
#     print(i)
    
    
# for i in range(1,5):           #Exclude 5         i=i+1
#     print('Hello')


# for i in range(1,10,5):           #increment        i=i+5
#     print('Hello')



# for i in range(1,5,2):           #increment        i=i+2         start(inclusive) and stop(Exclusive) 
#     print('Hello')



# my_list=[1,2,3,4,5]

# for i in my_list:
#     print(i)



# my_list=[1,2,3,4,5]

# for i in my_list:
#     if i==5:
#         print('yes')    


'''Important'''

# my_list=[1,2,3,4,5]

# for i in my_list:
#     if i==5:
#         print('yes')
#     else:
#         print('No')
        
'''Important'''       
        
# my_list=[1,2,3,4,5]

# for i in my_list:
#     if i==5:
#         found=1
#     else:
#         found=0

# if found==1:
#     print('yes')
# elif found ==0:
#     print('No')
    
    
# my_list=[1,2,3,4,5]

# for i in my_list:               #i=1,found=0
#     if i==6:                    #i=2,found=0
#         found=1                 #The loop is going to break after 5
#     else:
#         found=0

# if found==1:
#     print('yes')
# elif found ==0:
#     print('No')
    
    
    
    
# my_list=[1,2,3,4,5]

# for i in my_list:               #i=1,found=0
#     if i==2:                    #i=2,found=1
#         found=1
#     else:
#         found=0

# if found==1:
#     print('yes')
# elif found ==0:
#     print('No')
    
    
    
# my_list=[1,2,3,4,5]

# for i in my_list:               
#     if i==2:                    
#         print(i)
#         break
#     else:
#         print(i)