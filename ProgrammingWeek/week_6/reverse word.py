def reverse_word(message):
    b=message.split()
    txtbox=[]
    for i in b:
        reversed=i[::-1]#[start,stop,step]
        txtbox.append(reversed)
    return ' '.join(txtbox)#เชื่อมข้อมูลใน list โดยเอา' 'มาคั่น
print(reverse_word('hi my name is winnie'))