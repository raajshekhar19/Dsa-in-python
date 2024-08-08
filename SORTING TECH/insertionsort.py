def insersion_sort(l):
    for i in range(len(l)):
        j = i
        while j>0 and l[j]<l[j-1]:
            (l[j],l[j-1])=(l[j-1],l[j])
            j = j-1
        
    for i in  range(len(l)):
        print(l[i])
        
insersion_sort([2,8,7,4,1])

#iterate from the begning of arr
# for the first element do nothing
# then genrate a while loop if the j > 0 and the prev elem 
# is greater than the current element
# swap and j--