## q12
## decryption only for 4letter key

def inv(a,n):
    a=a%n
    for i in range(n):
        if (a*i)%n==1:
            return i

def adjoint(m):
    x=[[0]*len(m) for _ in range(len(m))]
    x[0][0]=m[1][1]
    x[0][1]=m[0][1]*(-1)
    x[1][0]=m[1][0]*(-1)
    x[1][1]=m[0][0]
    return x

def det(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

def matinv(m):
    d=inv(det(m),26)
    aj=adjoint(m)
    for i in range(len(m)):
        for j in range(len(m)):
            aj[i][j]*=d
    return aj
    

def decrypt(m,key):
    kinv=matinv(key)
    m1=len(m)
    m2=len(m[0])
    ans=[[0]*m2 for _ in range(m1)]
    for i in range(m1):
        for j in range(m2):
            z=0
            for k in range(m2):
                z+=int(m[i][k]*kinv[k][j])
            ans[i][j]=chr((z%26)+97)
    t=[]
    for i in ans:
        t.append(''.join(i))
    return ''.join(t)

def encrypt(m,key):
    m1=len(m)
    m2=len(m[0])
    ans=[[0]*m2 for _ in range(m1)]
    for i in range(m1):
        for j in range(m2):
            z=0
            for k in range(m2):
                z+=(m[i][k]*key[k][j])
            ans[i][j]=z
            ans[i][j]=(ans[i][j]%26)+97
    print(ans)
    for i in range(m1):
        for j in range(m2):
            ans[i][j] = chr(ans[i][j])
    t=[]
    for i in ans:
        t.append(''.join(i))
    return ''.join(t)

def convert(x):
    m1=len(x)
    m2=len(x[0])
    y=x
    for i in range(m1):
        for j in range(m2):
            a=ord(x[i][j])
            y[i][j]=a-97
    return y

def makemat(m,x):
    m1=(len(m)//x)
    if len(m)%x!=0:
        m1+=1
    mat=[[0]*x for _ in range(m1)]
    m=list(m)
    y=0
    for i in range(m1):
        for j in range(x):
            if y>=len(m):
                mat[i][j]='x'
                y+=1
            else:
                mat[i][j]=m[y]
                y+=1
    return mat

m=input("enter string: ")
print("enter dim of key: ")
m1=int(input())
m2=int(input())
same=m1
key=[[0]*m2 for _ in range(m1)]
ip=list(input("enter key: "))
ipx=0
for i in range(m1):
    for j in range(m2):
        key[i][j]=ip[ipx]
        ipx+=1
m=makemat(m,same)
print("input mat=",m," key=",key)
mn=convert(m)
keyn=convert(key)
print("after converting: mat=",mn," key=",keyn)
ct=encrypt(mn,keyn)
print("after encryption: ",ct)
ctn=makemat(ct,same)
ctn=convert(ctn)
print("after converting: mat=",ctn)
pt=decrypt(ctn,keyn)
print("after decryption: ",pt)
