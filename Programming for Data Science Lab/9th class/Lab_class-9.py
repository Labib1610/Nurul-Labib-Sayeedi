#substring search

# sentence = 'to be or not to be that is the question'
# print(sentence.count('to'))

# sentence = 'to be or not to be that is the question'
# print(sentence.count('to',12))
# print(sentence.count('to',2,12))

# sentence = 'to be or not to be that is the question'
# print(sentence.index('be'))

# print('THAT' in sentence)
# print('that' in sentence)
# print('th' in sentence)
# print('THAT' not in sentence)
# print(sentence.startswith('to'))
# print(sentence.endswith('question'))

# values = '1\t2\t3\t4\t5\t5'
# print(values.replace('\t', ','))

# letters = 'this is a text'
# str = 'hello;My name is ;Hennah'
# print(str.split(', '))
# print(letters.split())
# text = "apple,banana,orange,grape,peach"
# split_result = text.split(",", 2)
# print(split_result)

# def freq(str):
#     dict = {}
#     z = str.split()
#     for i in z:
#         count = 0
#         for j in z:
#             if i == j:
#                 count = count+1
#         dict[i] = count
#     return dict

# print(freq('This is a Lab Class.'))



# def word_frequency_counter(text):
#     text = text.lower()
#     words = text.split()
#     word_freq = {}
#     for word in words:
#         word_freq[word] = words.count()
#     return word_freq
# text = 'This is a text. This is a code'
# result = word_frequency_counter(text)
# print(result)

# person = {'name':'Sajid',
#           'age':30,
#           'address':{
#               'street':'Dhanmondi',
#               'city':'Dhaka'
#               'zipcode':'1205'

              
#         }
# }
# print('Name:',person['name'])
# print('Age:',person['age'])
# print('Address:',person['address'])
# print('Name:',person['name'])
# print('Name:',person['name'])
# print('Name:',person['name'])

# person = {'name':'Sajid',
#           'age':30,
#           'address':{
#               'street':'Dhanmondi',
#               'city':'Dhaka',
#               'zipcode':'1205'

              
#         }
# }
# print('Address:')
# for i,j in person['address'].items():
#     print(i.capitalize() + ':', j)

# n = int(input('How many items are there?: '))
# item = {}
# items = []
# for i in range(n):
#     #input details for each item
#     name = input('Enter the name of the item: ')
#     quantity = input('Enter the quantity of the item: ')
#     price = input('Enter the price of the item: ')

#     #create a dictionary for the current item
#     item = {'name':name,'quantity':quantity,'price':price}

#     #Append the current item to the list
#     items.append(item)
# print()
# print(items)
# print(items[0]['name'])
# print()

# search_query = input('Enter a search query (name,quantity,price)')
# for item in items:
#     print(item)
#     if item['name'] == search_query:
#         print('price of the searched item:',item['price'])



#f = open('sample.text','w')
# f = open('sample.text','w')
# f.write('Hello Python.\n')
# f.write('I am writing in a file.\n')
# f.close()