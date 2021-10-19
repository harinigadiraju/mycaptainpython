list = []
listp = []
n = int(input("enter the number of elements in the list : "))
for i in range(0,n):
    element = int(input())
    list.append(element)
    if(element>=0):
        listp.append(element)
    else:
        break

        print("list1 : {}".format(list)")
print ("list2 : {}".format(listp)")
