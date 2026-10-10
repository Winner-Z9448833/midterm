class Discount:
    def __init__ (self,price):
        self.price=price
    
    def discount(self):
        if self.price>=1000:
            return self.price-((self.price/100)*15)
        elif 999>=self.price>=500:
            return self.price-((self.price/100)*10)
        elif 499>=self.price>=300:
            return self.price-((self.price/100)*5)
        else:
            return self.price
        
    def change(self,dis):
        c=3000-dis
        bank=[1000,500,100,50,20]
        coin=[10,5,2,1,0.5,0.25]
        bcount=[]
        ccount=[]
        countb,countc=0,0
        
        for i in bank:
            count=0
            while c>=i:
                c-=i
                count+=1
            bcount.append(count)
        for j in coin:
            count=0
            while c>=j:
                c-=j
                count+=1
            ccount.append(count)
        for i in bank:
            if bcount[countb]!=0:
                print(f' {i}:\t{bcount[countb]} ใบ')
            countb+=1
        for i in coin:
            if ccount[countc]!=0:
                print(f' {i}:\t{ccount[countc]} เหรียญ')
            countc+=1
                    
d=Discount(int(input('price: ')))
dis=d.discount()
print(f'ราคา-ส่วนลด: {dis}')
print('จ่ายมา: 3000')
print(f'ทอน:')
d.change(dis)
