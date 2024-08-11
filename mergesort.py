#merge sort

#recc..
#merge function
#split

def merge(A,B):                 # merge A[0:m] , B[0,n]
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i + j< m+n:
        if i==m :
            C.append(B[j])
            j = j+ 1
        elif j== n:
            C.append(A[i])
            i = i +1
        elif A[i]<=B[j]:
            C.append(A[i])
            i = i+ 1
        elif A[i]>B[j]:
            C.append(B[j])
            j = j + 1
    return(C)

def mergesort(A,left,right) :
    # Sort the slice A [left:right]
    if right - left <=1:
        return (A[left:right])
    if right - left >1 :
        mid = ( left + right )//2
        L = mergesort(A,left,mid)
        R = mergesort(A, mid,right)
        return (merge(L,R))
    
a = list(range(1,100,2)) + list(range(0,100,2))
print(a)
print(mergesort(a,0,len(a)))