# my_list1 = [1,2,3,4,5]
# even_list = []
# odd_list = []

# for i in my_list1:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(even_list)
# print(odd_list)

#remove the odd number from even_list and even number from odd_list then insert the even number in even_list and odd number in odd_list from my_list1 

# my_list1 = [1,2,3,4,5]
# even_list = [1,2,3,4,5]
# odd_list = [1,2,3,4,5]

# for i in my_list1:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)

# for i in even_list:
#     if i % 2 !=0:
#         even_list.remove(i)
# for i in odd_list:
#     if i % 2 ==0:
#         odd_list.remove(i)
# print(even_list)
# print(odd_list)

'''Important'''

# my_list1 = [1,2,3,4,5]

# for i in range(len(my_list1)):
#     for x in my_list1:
#         if x%2==0:
#             my_list1[i] = 0
#             break 
            
#         else:
#             my_list1[i] = 1
#             break
#     break
# print(my_list1)

'''This way'''

# my_list1 = [1,2,3,4,5]

# for i in range(len(my_list1)):

#     if my_list1[i]%2==0:
#             my_list1[i] = 0
            
            
#     else:
#             my_list1[i] = 1
            
# print(my_list1)


# my_list1 = [1,2,3,4,5]


# for x in my_list1:
#         if x%2==0:
#             my_list1.replace(x,1)
             
            
#         else:
#             my_list1.replace(x,0)
# print(my_list1)


# count = 1
# while count<=5:
#     print(count)
#     count+=1
# print(count)

# count = 10
# while count>=0:
#     print(count)
#     count-=1
# # print(count)
    

# count = 10
# while count>=0:
#     print(count,end=',')
#     count-=1


# count = 10
# while count>=0:
#     if count!=8:    
#         print(count,end=',')
#     count-=1


# count = 1
# muliplication = 2
# while count<=10:
#     if count != 3:    
#         print(muliplication*count)
#     count+=1


# count = 0
# muliplication = 2
# while count<=10:
#     count+=1
#     if count == 3:
#         continue    
#     print(f'{muliplication}*{count} = {muliplication*count}')

'''Different way'''

# i = 1
# while i <=10:
#     if i == 3:
#         i = i+1
#         continue
#     print(f'2X{i}={2*i}')
#     i = i+1




# while True:                                       #if else er coffee er program       ///    password wrong hole
#     string = input('Enter any string: ')
#     if string.lower() == 'quit':
#         break
#     print(string)

# count = 0
# muliplication = '*'
# while count<=10:
#     count +=1
#     print(muliplication*count)


# my_list = ['Hello','World','Sunday']

# search_word = input("Enter any word from list: ")

# replace_word = input("Enter any word from list: ")

# for i in range(len(my_list)):
#     if search_word.title() in my_list:
#         my_list[index(search_word.title())] = replace_word.title()
# print(my_list)


# my_list = ['Hello','World','Sunday']

# search_word = input("Enter any word from list: ")

# replace_word = input("Enter any word from list: ")

# for i in range(len(my_list)):
#     if search_word.title() == 'Hello':
#         my_list[0] = replace_word.title()
#     if search_word.title() == 'World':
#         my_list[1] = replace_word.title()
#     if search_word.title() == 'Sunday':
#         my_list[2] = replace_word.title()
# print(my_list)



# my_list = ['Hello','World','Sunday']
# search_word = input("Enter any word from list: ")
# replace_word = input("Enter any word from list: ")
# for i in range(len(my_list)):
#     if (my_list[i]==search_word):
#         my_list[i] = replace_word
# print(my_list)


# my_list = ['Hello','World','Sunday','World','World']
# search_word = input("Enter any word from list: ")
# replace_word = input("Enter any word from list: ")
# i=0
# while i< len(my_list):
#     if (my_list[i]==search_word):
#         my_list[i] = replace_word
#         i+=i
#     i+=i
# print(my_list)