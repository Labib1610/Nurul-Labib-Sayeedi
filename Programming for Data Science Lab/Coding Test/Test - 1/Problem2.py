Amount = int(input('Enter the amount: '))

if 1000<=Amount:                         #1256
    _1000=(Amount//1000)                 #  = 1
    print('1000 taka notes:',_1000)
    changed1 = Amount -  _1000*1000      #1256-1*1000 = 256
else:                                   #False
    print('1000 taka notes:',0)
    changed1 = Amount
if 500<=changed1:                     #False
    _500=(changed1//500)
    print('500 taka notes:',_500)
    changed2 = changed1 -  _500*500
else:                              #True
    print('500 taka notes:',0)             
    changed2 = changed1            #changed2=256
if 200<=changed2:                    #256
    _200=(changed2//200)             # =2
    print('200 taka notes:',_200)    
    changed3 = changed2 -  _200*200         #changed3= 256-
else:
    print('200 taka notes:',0)
    changed3 = changed2
if 100<=changed3:
    _100=(changed3//100)
    print('100 taka notes:',_100)
    changed4 = changed3 -  _100*100
else:
    print('100 taka notes:',0)
    changed4 = changed3
if 50<=changed4:
    _50=(changed4//50)
    print('50 taka notes:',_50)
    changed5 = changed4 -  _50*50
else:
    print('50 taka notes:',0)
    changed5 = changed4
if 20<=changed5:
    _20=(changed5//20)
    print('20 taka notes:',_20)
    changed6 = changed5 -  _20*20
else:
    print('20 taka notes:',0)
    changed6 = changed5
if 10<=changed6:
    _10=(changed6//10)
    print('10 taka notes:',_10)
    changed7 = changed6 -  _10*10
else:
    print('10 taka notes:',0)
    changed7 = changed6
if 5<=changed7:
    _5=(changed7//5)
    print('5 taka notes:',_5)
    changed8 = changed7 -  _5*5
else:
    print('5 taka notes:',0)
    changed8 = changed7
if 2<=changed8:
    _2=(changed8//2)
    print('2 taka notes:',_2)
    changed9 = changed8 -  _2*2
else:
    print('2 taka notes:',0)
    changed9 = changed8
if 1<=changed9:
    _1=(changed9//1)
    print('1 taka notes:',_1)
    changed10 = changed9 -  _1*1
else:
    print('1 taka notes:',0)
    changed10 = changed9