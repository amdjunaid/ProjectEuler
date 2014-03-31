import math
def twofactors(i,j):
#    print("b")
#    c=False
    sq=math.sqrt(i*j)
    if ((i>=sq) and (j<=sq)) or ((i<=sq) and (j>=sq)):
        return True
    else:
        return False

def check_palindrome(i):
#    print("uhuh")
    st=str(i)
    l=[]
    c=0
    for x in range(len(st)):
        l.append(st[x])
    start=0
    end=len(l)-1
    if len(l)%2==0:
        while True:
            if (start-end)==1:
                if l[start]==l[end]:
                    c=0
                    break;
            else:
                if l[start]==l[end]:
                    start+=1
                    end-=1
                    c=0
                else:
                    c=1
                    break
        if c==0:
            #print("True")
            return True
        else:
            return False
    else:#odd length
        while True:
            if start==end:
                if l[start]==l[end]:
                    c=0
                    break
            else:
                if l[start]==l[end]:
                    start+=1
                    end-=1
                    c=0
                else:
                    c=1
                    break
        if c==0:
            return True
        else:
            return False
max=0
for i in range(99,0,-1):
    for j in range(99,0,-1):
        if check_palindrome(i*j):
            if twofactors(i,j):
                pal=i*j
                if max<pal:
                    max=pal
print(max)
