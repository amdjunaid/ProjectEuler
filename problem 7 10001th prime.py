import math
primes=[] #list of primes
for i in range(40000001):
    primes.append(1) # assuming all numbers to be prime in beginning
primes.insert(0,0) #0 isnt prime
primes.insert(1,0) #1 isnt prime
i=2
while i<=math.sqrt(40000001):
    j=2
    if primes[i]==1:
        while i*j<=40000001:
            primes[i*j]=0
            j+=1
    i+=1
c=0
for i in range(2,40000000):
    if primes[i]==1:
        c+=1
    if(c==10001):
        print(i)
        break

            
