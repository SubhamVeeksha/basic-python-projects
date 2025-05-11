#while-loop for factorial

#n=int(input("n:"))
#factorial=1
#while n>0:
 #   factorial=factorial*n
  #  n-=1
#print(factorial)

#for-loop for factorial
n=int(input("n:"))
factorial=1
for i in range(1,n):
    factorial=factorial*n
    n-=1
print(factorial)