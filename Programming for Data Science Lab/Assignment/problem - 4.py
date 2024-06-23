sample_dict = {
                "name": "Kelly",
                "age": 25,
                "salary": 8000,
                "city": "New york"
}
dictionary = {}
keys = ['name','salary']
for i in sample_dict.keys():
  if i in keys:
    dictionary[i]=sample_dict[i]
print(dictionary)