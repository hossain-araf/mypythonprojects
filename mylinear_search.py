def linear_watch(list,shot):
    for a in range(0,len(list)):
        if list[a]==shot:
            return a 
            return None

def again_veryfy(gotya):
    if gotya is not None:
        print("target found in the list:",gotya)
    else:
        print("Target not found in the list")


mylist=[1,2,3,34,5,6,78,89,0,1333]
j=linear_watch(mylist,34)
again_veryfy(j)