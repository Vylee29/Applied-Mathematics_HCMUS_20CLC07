def Input():
    n=int(input("Input n: "))
    m=int(input("Input m: "))
    lst = [] 

    for i in range(3):
        lst.append([]) 
        for j in range(3): 
            x=int(input("nhap x: "))
            lst[i].append(x) 
        
    print(lst) 

def swap(a,b):
    c=[]
    for i in range (len(a)):
        c.append(a[i])
        a[i]=b[i]
        b[i]=c[i]
def Gauss(a):
        i=0
        for j in range(len(a[0])-1):
            if a[i][j]!=0:
                x=a[i][j]
                for n in range(len(a[0])):
                    a[i][n]/=x
            if a[i][j]==1:
                k=i
                for n in range(i+1,len(a)):
                    x=a[n][j]
                    for m in range(j,len(a[0])):
                        a[n][m]-=x*a[i][m]
            elif a[i][j]==0:
                for h in range (i+1,len(a)):
                    swap(a[i],a[h])
                    break
            i+=1
            if(i==len(a)):
                break
            
                    
def main():
    a=[[4,-2,-4,2,1],[6,-3,0,-5,3],[8,-4,28,-44,11],[-8,4,-4,12,-5]]
    print(a)
    Gauss(a)
    print(a)
main()

        
