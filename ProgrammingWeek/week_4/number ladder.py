num=int(input('number: '))
row=1
while num>0:
    colum=1
    while colum<=row:
        print(colum,end=' ')
        colum+=1
    print()
    row+=1
    num-=1