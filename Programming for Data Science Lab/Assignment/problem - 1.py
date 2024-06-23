dictionary= {'Math':81,
             'Physics':83,
             'Chemistry':87, 
}

SortedList = sorted(dictionary.items(),key=lambda x:x[1],reverse = True) 
print(SortedList)