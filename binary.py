def binary_search(list,target):
    first=0
    last=len(list)-1
    midpoint=(first+last)//2
    if list[midpoint]==target:
        return midpoint
    elif list[midpoint] < target:
        first=midpoint+1
    else:
        first=midpoint-1
        return midpoint
        return None



def c(index):
    if index is not None:
        print("yes")
    else:
        print("not found")


n=[1,2,,3,4,5,6,7,8,9,10]
j=binary_search(n,67)
c(j)

