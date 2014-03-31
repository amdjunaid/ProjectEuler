st=input()
c=1
list=[int(x) for x in st.split("\n")]
x=0
for l in list:
    x+=l
st=str(x)
#print(st)
print(st[:10])
