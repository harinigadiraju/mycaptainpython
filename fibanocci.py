n = int(input("enter number of terms in the series"))
n1 = 0
n2 = 1
i = 0
if(n<=0):
  print("only positive integers accepted")
elif(n==1):
  print(n1)
else:
  print("the fibanocci series with {} terms :".format(n))
  while i<n :
    print( n1)
    n3 = n1 + n2 
    n1 = n2
    n2 = n3
    i = i + 1
