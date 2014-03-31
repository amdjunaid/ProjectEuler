import math
c=0
for i in range(2,50):
    c=0
    for j in range(2,50):
        if i%j==0:
            c=1
            break
    if c==1:
        continue
    elif c==0:
        print("Prime number:",i)
    else:
        print("hello")
    
