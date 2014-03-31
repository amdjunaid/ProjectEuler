a=1
b=2
sum=2
c=a+b
while c<4000000:
    a=b
    b=c
    c=a+b
    if c%2==0:
        sum+=c
print(sum)
