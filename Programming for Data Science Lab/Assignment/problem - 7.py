A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dictionary = {}
for i in A:
  if i%2!=0:
    dictionary[i]=i*i
print(dictionary)