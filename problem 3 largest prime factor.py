x=int(input())
i=2
max=2
while x>1:
   if x%i==0: # if i is divisor
      x/=i
      max=i# current max divisor which is by default a prime
      #print("value:",x,"i:",max)
   else: #if i is not a divisor
      i+=1
print(max)
    
