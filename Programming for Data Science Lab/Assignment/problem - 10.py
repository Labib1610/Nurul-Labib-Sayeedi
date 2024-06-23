def is_prime(x):
    a = False
    prime = 0
    for i in range(1,x+1):
        if x%i==0:
            prime+=1
    if prime==2:
        a = True
    return a 
n=int(input("Input= "))
def perfectPrime(x):
    list=[]
    for i in range(2,n+1):
        if is_prime(i) and i!=2:
            if x**i<100:
                list.append(x**i)
    return list
Dictionary={}
for i in range(1,n+1):
    if is_prime(i):
        if perfectPrime(i):
            Dictionary[i]=perfectPrime(i)
print("Output:\n",Dictionary)