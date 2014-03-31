x=input()
i=0
max=0
k=0
list=[int(y) for y in x]
while True:
    if(i>(len(list)-5)):#if final
        break
    else:
        High=False
        sum=1
        for j in range(5):
            if list[i+j]==0:
                k=j
                High=True
                break
        if(High==True):# if 0 is found,skip k+1 steps
            i+=(k+1)
        else:# if 0 is not found
            for j in range(5):#calculate the mul val
                sum*=list[i+j]
            if max<sum:# check the max value
                max=sum
            i+=1
print(max)
