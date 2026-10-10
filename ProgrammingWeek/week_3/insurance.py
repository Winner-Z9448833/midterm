def insurance(a,b):
    base=10000
    if a<25:
        if b==1:
            base+=base*50/100
        elif b==2:
            base+=base*20/100
    else:
        if b==1:
            base+=base*10/100
        elif b==2:
            base-=base*15/100  
    return base
while True:
    try:
        age=int(input('your age: '))
        accident=int(input('(1) for YES\n(2) for NO\nYou ever have accident?: '))
        if accident !=1 and accident !=2:
            print('### 1 or 2 only for accident ###')
            continue
        elif age<=0 or accident<=0:
            print('### it can not be less than or equal 0 ###')
            continue
        result=insurance(age,accident)
        print(f'The premium totals {result}')
    except:
        print('Pls try again')