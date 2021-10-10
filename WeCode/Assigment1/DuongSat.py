k, t= map(int, input().split())

n=t//k
du=t%k
if(n%2==0):
  print(du)
else:
  print(k-du)