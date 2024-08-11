def quick_sort(A,l,r):  # sort A[l:r]
    if r - l < 1 :      # partition w.r.t pivot
        return()
    
    #partition w r t A[l]
    
    yellow = l + 1
    
    for green in range(l+1,r):
        if A[green]<=A[l]:
            (A[green],A[yellow])=(A[yellow],A[green])
            yellow = yellow + 1
    
    (A[l],A[yellow-1])=(A[yellow-1],A[l])
    quick_sort(A,l,yellow-1)
    quick_sort(A,yellow,r)    