from datetime import datetime
def collatz(x):
    c=1
    y=x
    while y>1:
        c+=1
        if y%2==0:
            y=y/2
        else:
            y=3*y+1
    return c
startTime = datetime.now()
print("Optimised Collatz")
x=int(input("Upper Limit"))
y=int(input("Lower Limit"))
max_count=0
max_iter=0
steps=0
for i in range(x-1,int((x-1)/2),-2):
    steps+=1
    count=collatz(i)
    if max_count<=count:
        max_count=count
        max_iter=i
print("Max_Iter:",max_iter,"Max_count:",max_count)
print("Total Steps:",steps)
print(datetime.now()-startTime)
