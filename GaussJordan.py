def swap(a,b):
    c=[]
    for i in range (len(a)):
        c.append(a[i])
        a[i]=b[i]
        b[i]=c[i]
def createMatrixI(a):
    c=[]
    b=[]
    for i in range (len(a)):
        b.append([])
        for j in range (len(a[0])):
            if i==j:
                b[i].append(1)
            else:
                b[i].append(0)
    return b
    
def Gauss(a,b):
        # i chạy từng dòng 
        # j nhảy qua từng cột
        i=0
        for j in range(len(a[0])):
            # nếu a[i][j] khác 0 thì chia dòng đó cho a[i][j]
            if a[i][j]!=0:
                chia=a[i][j]
                for n in range(len(a[0])):
                    a[i][n]/=chia
                    b[i][n]/=chia
            # nếu a[i][j] nhảy xuống dòng tiếp theo để chia những số dưới về 0
            if a[i][j]==1:
                k=i
                for n in range(i+1,len(a)):
                    chia=a[n][j]
                    for m in range(len(a[0])):
                        a[n][m]-=chia*a[i][m]
                        b[n][m]-=chia*b[i][m]
            # nếu a[i][j] ==0 thì swap với dòng dưới khác 0, nếu tất cả =0 thì nhảy qua cột bên cạnh  để thực hiện
            elif a[i][j]==0:   
                for h in range (i+1,len(a)):
                    if a[h][j]!=0:
                        swap(a[i],a[h])
                        swap(b[i],b[h])
                        break
                if a[i][j]==0:
                    i=i-1
            i+=1
            if(i==len(a)):
                break

def inverse(a): 
    # tạo ra ma trận đơn vị của ma trận a
    b=createMatrixI(a)
    # biến ma trận thành ma trận bậc thang bằng cách sử dụng gauss
    Gauss(a,b)
    #print(a)
    dt=1
    # để có công thức định thức
    # các phần tử tại vị trí thứ (0,0),(1,1),... của ma trận ta nhân chúng lại với nhau 
    for i in range (len(a))  :
        dt*= a[i][i]

    # nếu định thức = 0 ma trận không khả nghịch 
    # ngược lại định thức khác 0 ta sử dụng phép tính biến đổi sơ cấp trên dòng 
    # biến các phần tử trong cùng cột khác 1 = 0 để ra ma trận khả nghịch 
    if dt==0:
        print('Det = 0')
        print('Ma tran khong kha nghich')
        return 0
    else:
        for i in range (len(a)):
            if a[i][i]==1:
                n=i-1
                while n>=0:
                    h=a[n][i]
                    for k in range (len(a)):
                        a[n][k]=a[n][k]-(a[i][k]*h)
                        b[n][k]=b[n][k]-(b[i][k]*h)
                    n-=1
    return b
    
                  
def main():
    a=[[1,-1,2],[1,1,-2],[1,1,4]]
    print('Test Matrix 1: ')
    b=inverse(a)
    if b!=0:
        print(b)
    
    

    matrix2=[[1,2,1],[3,7,3],[2,3,4]]
    print('Test Matrix 2: ')
    submatrix2=inverse(matrix2)
    if submatrix2!=0:
        print(submatrix2)


    matrix3=[[1,2,3],[2,5,3],[1,0,8]]
    print('Test Matrix 3: ')
    submatrix3=inverse(matrix3)
    if submatrix3!=0:
        print(submatrix3)
   

if __name__ == "__main__":
    main()
                

