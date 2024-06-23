dictionary={}
for i in "w3resource":
  count=0
  for j in "w3resource":
    if i == j:
      count+=1
    dictionary[i]=count
print(dictionary)