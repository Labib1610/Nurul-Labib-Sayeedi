Thriller = int(input('Enter the quantity of thriller books: '))
Adventure = int(input('Enter the quantity of adventure books: '))
Action = int(input('Enter the quantity of action books: '))
Romance = int(input('Enter the quantity of romance books: '))
Mystery = int(input('Enter the quantity of mystery books: '))

Total_Price = (Thriller*200)+(Adventure*180)+(Action*220)+(Romance*150)+(Mystery*170)

Discount_Price = (Total_Price-Total_Price/10)

if 1000<=Total_Price:
    print("Total price after discount: ",Discount_Price)
else:
    print('Your Total price is: ',Total_Price)


