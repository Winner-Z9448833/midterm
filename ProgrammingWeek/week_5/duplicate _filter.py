def dup_check(box):
    a=box
    new=[]
    i=0
    while len(a)>i:
        if a[i] not in new:
            new.append(a[i])
        i+=1
    return new


box=[]
while True:
    try:
        num=input(f'\'exit\'for stop loop num: ')
        if num=='exit':
            break
        num=int(num)
        box.append(num)
    except:
        print('try again')
print(box)
result=dup_check(box)
print(result)