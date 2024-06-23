A = "the quick brown fox jumps over the lazy dog the lazy dog barks"
x = A.split()
print(x)
dictionary={}
for i in x:
  count = 0
  for j in x:
    if i == j:
      count+=1
  dictionary[i]=count
print(dictionary)