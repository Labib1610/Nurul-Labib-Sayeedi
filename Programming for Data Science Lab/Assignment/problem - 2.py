list1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
dictionary={}
for i in list1:
  if i['item'] in dictionary.keys():
    dictionary[i['item']]+=i['amount']
  else:
    dictionary[i['item']]=i['amount']
print(dictionary)