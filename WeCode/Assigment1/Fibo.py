def F(n):
    if n == 1 or n == 2:
        return 1
    return F(n - 1) + F(n - 2)

n=int(input())

if(n<1 or n>30):
  print('So '+str(n)+' khong nam trong khoang [1,30].')
else:
  print(F(n))