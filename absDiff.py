def diffvalue(arr,num,diff):
    count=0
    for i in range(len(arr)):
        if(abs(num-arr[i])<=diff):
            count+=1
    if count>0:
         return count
    else:
         return -1
arr=[12,3,14,56,77,13]
num=int(input("enter number"))
diff=int(input("enter difference"))
print(diffvalue(arr,num,diff))
