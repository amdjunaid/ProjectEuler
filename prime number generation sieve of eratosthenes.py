import math
primes=[] #list of primes
for i in range(2000001):
    primes.append(1) # assuming all numbers to be prime in beginning
primes.insert(0,0) #0 isnt prime
primes.insert(1,0) #1 isnt prime
i=2
while i<=math.sqrt(2000000):
    j=2
    if primes[i]==1:
        while i*j<=2000001:
            primes[i*j]=0
            j+=1
    i+=1
sum=0
for i in range(2000000,1,-1):
    if primes[i]==1:
        sum+=i
print(sum)
