n = int(input('Enter the number of rows: ')) 



for i in range(n,0,-1):
    for j in range(i,i**2+1,i):
        print(j,end=' ')
        
    print()
