st=input("Enter the sting:")
n=int(input("Enter the 0 if it is left rotation enter 1 if it is right rotation :"))
while True:
    if n==0 or n==1:
        break
    else:
        n = int(input("Enter the 0 if it is left rotation enter 1 if it is right rotation :"))
c=int(input("Enter the number of times you want to rotate :"))
for i in range(c):
    if n==0:
        st=st[1:]+st[0]

    elif n==1:
        st=st[-1]+st[0:-1]


print(st)