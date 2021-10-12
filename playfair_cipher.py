def decrypt(i1,i2,j1,j2,mat):
    if i1==j1:
        i2=(i2-1)%5
        j2=(j2-1)%5
    elif i2==j2:
        i1=(i1-1)%5
        j1=(j1-1)%5
    else:
        t=i2
        i2=j2
        j2=t
    return [mat[i1][i2],mat[j1][j2]]

def encrypt(i1,i2,j1,j2,mat):
    if i1==j1:
        i2=(i2+1)%5
        j2=(j2+1)%5
    elif i2==j2:
        i1=(i1+1)%5
        j1=(j1+1)%5
    else:
        t=i2
        i2=j2
        j2=t
    return [mat[i1][i2],mat[j1][j2]]

def geti(x,mat):
    for i in range(5):
        for j in range(5):
            if mat[i][j]==x:
                return i,j

def getpair(m):
    pair=[]
    x=0
    while x<len(m):
        if len(m)<x+1:
            pair.append([m[x],'x'])
            x+=1
        elif m[x]!=m[x+1]:
            pair.append([m[x],m[x+1]])
            x+=2
        else:
            pair.append([m[x],'x'])
            x+=1
    return pair


def transform(m,mat,s):
    pair=getpair(m)
    if s=='encrypt':
        print("for encryption: ",pair)
    else:
        print("for decryption: ",pair)
    t=[]
    for i in pair:
        i1,i2=geti(i[0],mat)
        j1,j2=geti(i[1],mat)
        if s=='encrypt':
            y=encrypt(i1,i2,j1,j2,mat)
        elif s=='decrypt':
            y=decrypt(i1,i2,j1,j2,mat)
        t.append(y)
    t1=[]
    for i in t:
        t1.append(''.join(i))
    return ''.join(t1)

def validInput(m,replace):
    m=list(m)
    m=[replace[1] if x==replace[0] else x for x in m]
    return m

def validOutput(m):
    m=list(m)
    f=[]
    for i in range(len(m)):
        if m[i]=='x' and i!=0 and i!=len(m)-1:
            if m[i-1]==m[i+1]:
                f.append(i)
    for i in f:
        del m[i]
    return ''.join(m)
    

def makematrix(key,list1,mat):
    k=list(set(key))
    x=0
    for i in range(5):
        for j in range(5):
            if x<len(k):
                mat[i][j]=k[x]
                list1.remove(k[x])
                x+=1
    replace=[list1[-1],list1[-2]]
    list1.remove(replace[0])
    x=0
    for i in range(5):
        for j in range(5):
            if mat[i][j]==0:
                mat[i][j]=list1[x]
                x+=1
    return mat,replace

def printmat(mat,replace):
    for i in range(5):
        for j in range(5):
            if mat[i][j]==replace[1]:
                print(replace[0],'/',replace[1])
            else:
                print(mat[i][j])
        print
                

list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mat=[[0]*5 for _ in range(5)]
m=input("enter message: ")
key=input("enter key: ")
mat,replace = makematrix(key,list1,mat)
printmat(mat,replace)
m=validInput(m,replace)
ct=transform(m,mat,'encrypt')
print("after encryption: ",ct)
pt=transform(ct,mat,'decrypt')
pt=validOutput(pt)
print("after decryption: ",pt)
