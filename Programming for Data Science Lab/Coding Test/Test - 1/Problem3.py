Beverage = input('Enter your preferred beverage(Coffee,Tea,Juice):')
Size = input('Enter your preferred size(Small,Medium,Large):')

if Beverage == 'Coffee':
    if Size == 'Small':
        print(f'Price: {50} TK')
    elif Size == 'Medium':
        print(f'Price: {80} TK')
    elif Size == 'Large':
        print(f'Price: {100} TK')
elif Beverage == 'Tea':
    if Size == 'Small':
        print(f'Price: {40} TK')
    elif Size == 'Medium':
        print(f'Price: {60} TK')
    elif Size == 'Large':
        print(f'Price: {80} TK')
elif Beverage == 'Juice':
    if Size == 'Small':
        print(f'Price: {60} TK')
    elif Size == 'Medium':
        print(f'Price: {70} TK')
    elif Size == 'Large':
        print(f'Price: {90} TK')