import math

def square(a,b,c):
  p=(a+b+c)/2
  return math.sqrt(p*(p-a)*(p-b)*(p-c))

a=float(input())
b=float(input())
c=float(input())
S=square(a,b,c)
if(S%2==0 or S%2==1):
  S=int(S)
else:
  S=round(S,2)
if( a<b+c and b<a+c and c<a+b ):
        if( a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b):
            print('Tam giac vuong, dien tich = '+str(S))
        elif(a==b and b==c):
            print('Tam giac deu, dien tich = '+str(S))
        elif(a==b or a==c or b==c):
            print('Tam giac can, dien tich = '+str(S))
        else:   
            print('Tam giac thuong, dien tich = '+str(S))
else:
        print('Khong phai tam giac')