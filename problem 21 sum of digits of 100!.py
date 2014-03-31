def fact(n):
    sum=1
    if n>1:
        sum=sum*n
        return sum*fact(n-1)
    return sum
st=str(fact(100))
sum=0
for i in st:
    sum+=int(i)
print(sum)
