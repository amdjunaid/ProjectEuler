primes=[]
for i in range(2,101):
    primes.insert(i,1)
primes[0]=0
primes[1]=0
for i in range(2,101):
    j=2
    if primes[i]==1:
        while i*j<=100:
            primes.insert((i*j),0)
            j+=1
for i in range(101):
    if primes[i]==1:
        print(i)
