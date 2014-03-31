from datetime import datetime
def fact(n):
    sum=1
    if n>1:
        sum=sum*n
        return sum*fact(n-1)
    return sum
startTime = datetime.now()
factorial={}
for i in range(10):
    factorial[i]=fact(i)
i=10
sum_major=0
while i<9999999:
    st=str(i)
    sum_minor=0
    for j in range(len(st)):
        sum_minor+=factorial[int(st[j])]
        if sum_minor>i:
            break
    if sum_minor==i:
        sum_major+=i
    i+=1
print(sum_major)
print(datetime.now()-startTime)
