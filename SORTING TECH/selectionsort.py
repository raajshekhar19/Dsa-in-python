#iterate in the whole list
# assign min to the iterator
# iterate again from the iterator to the rest part of the arr
# if any elemet is found less than the element then swap


def selection_sort(l):
    for start in range(len(l)):
        minpos = start
        for i in range (start,len(l)):
            if l[i] < l[minpos] :
                minpos = i
        (l[start],l[minpos])=(l[minpos],l[start])
    
    for i in range (len(l)):
        print(l[i]) 
               


selection_sort([6,7,2,1])