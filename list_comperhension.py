#single one line code
# s=[x**2 for x in range (1,11)]
#print(s)
# output:[1,4,9,16,25,36,49,64,81,100]
#similarly we can write upto 100 or 500 as we wish.


#converting output into string
# inp=input().split()
#l=[]
#print(inp)
#Expected input: 1 2 3 4 5 
# output:[1, 2, 3, 4, 5]


#converting output into intergers
#i=input().split()
#l=[int(item) for item in i]
#print(l)
#Expected input:1 2 3 4 5 
#output:[1, 2, 3, 4, 5]


#square of specific numbers
a=input().split()
l=[(int(item))**2 for item in a]
print(l)
#expected input:1 2 3 4 5 6 
#output:[1, 4, 9, 16, 25, 36]