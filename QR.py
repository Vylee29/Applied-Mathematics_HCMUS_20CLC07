#MSSV:20127392
#Ho ten: Le Nguyen Lan Vy
#Lop: 20CLC07
import math

def convertMatrix(a):
    #thanh lap ma tran chuyen vi v
    i=0
    v=[]

    for i in range (len(a[0])):
        v.append([])
        for j in range (len(a)):
            v[i].append(a[j][i])

    return v

def distanceOf2Vecto (a,b):
    #tinh khoang cach 2 vecto<a,b>
    sum=0
    for i in range (len(a)):
        sum+=(a[i]*b[i])
    return sum

def sumOfList (a,b):
    #tinh tong hai list
    sum=[]
    for i in range (len(a)):
        sum.append(a[i]+b[i])
    return sum
def subtractOfList (a,b):
    #tinh hieu cua hai list
    sum=[]
    for i in range (len(a)):
        sum.append(a[i]-b[i])
    return sum    
def caculateQ(v):
    #tinh ra duoc ma tran Q
    l=[]
    sum=[]
    q=[]
    for p in range (len(v[0])):
        sum.append(0)
        l.append(0)
    u=[]

    for i in range (len(v)):
        q.append([])
        u.append([])
        if i==0:
            for j in range (len(v[i])):
                u[i].append(v[i][j])
        else:
            for j in range (i):
                m=distanceOf2Vecto(v[i],u[j])/distanceOf2Vecto(u[j],u[j])
                for n in range (len(u[j])):
                    l[n]=m*u[j][n]
                sum=sumOfList(sum,l)
            tru = []
            tru = subtractOfList(v[i],sum)
            for j in range (len(tru)):
                u[i].append(tru[j])
            for p in range (len(v[0])):
                sum[p] = 0
        x=1/math.sqrt(distanceOf2Vecto(u[i],u[i]))
        for k in range (len(u[i])):
            q[i].append(x*u[i][k])
    
    return q

def caculateR (q,a)   :
    q=convertMatrix(q)
    r=[]
    for g in range (len(a)):
        r.append([])
        r[g].append(q*a[g])
    return r

def main():
   a=[[1,1,2],[2,-1,1],[-2,4,1]]
   v=convertMatrix(a)
   q=caculateQ(v)
   print(q)
   #r=caculateR(q,a)
   #print r

   b=[[1,1,1],[2,-2,2],[1,1,-1]]
   m=convertMatrix(b)
   q1=caculateQ(m)
   print(q1)

   c=[[1,1,1],[2,-2,2],[1,1,-1]]
   n=convertMatrix(c)
   q2=caculateQ(n)
   print(q2)

if __name__ == "__main__":
    main()
                