# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=' ')
#     print()



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


# for i in range(5):
#     for j in range(1,6-i):
#         print(j,end=' ')
#     print()
    
    
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(j,end=' ')
#     print()


# list1 = ['Sunday','Monday','Tuesday']
# list2 = ['January','February','March']
# for x in list1:
#     for y in range(len(list2)):
#         print(list2[y])
#         print(list1[y])
        
        

# list1 = ['Sunday','Monday','Tuesday']
# list2 = ['January','February','March']
# for x in list1:
#     for y in list2:
#         print(y)
#         print(x)
        
        

# list1 = ['Sunday','Monday','Tuesday']
# list2 = ['January','February','March']
# for x in list1:
#     for y in list2:
#         print(y)
#         print(x)
#     print()
#     print()


# list1 = ['Sunday','Monday','Tuesday']

# for x in list1:
#     count = 0
#     for y in x:
#         count = count+1
#     print(f'Total number of character in {x} is {count}')



# list1 = ['Sunday','Monday','Tuesday']
# vow = 'aeiouAEIOU' 
# for x in list1:
#     vowel = 0
#     for y in x:
#        if y.lower() in vow: 
#         vowel = vowel+1
#     print(f'Total number of Vowel in {x} is {vowel}')
    
    
list1 = ['Sunday','Monday','Tuesday']
vow = ['a','e','i','o','u'] 
for x in list1:
    vowel = 0
    for y in x:
       if y.lower() in vow: 
        vowel = vowel+1
    print(f'Total number of Vowel in {x} is {vowel}')