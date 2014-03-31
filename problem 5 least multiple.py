i=380
a=[11,12,13,14,16,17,18]
c=0
val=i
while True:
    c=0
    for j in a:
        if i%j==0:
            c+=1
    if(c==len(a)):
        val=i
        break
    else:
        i+=380
print(val)
