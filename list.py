def common_elements(arr1,arr2,arr3):
    i=j=k=0
    result=[]
    while i<len(arr1) and j<len(arr2) and k<len(arr3):
        if arr1[i]==arr2[j]==arr3[k]:
            if not result or result[-1] != arr1[i]:
                # true last element and current element is same then ignore it diffrent add
                result.append(arr1[i])
            #step1 : i=0,j=0,k=0
            # arr1[i]=1,arr2[j]=2,arr3[k]=5
            # 1==2==3 not same then go to else bloack
            #step2 : i=1,j=0,k=0
            # arr1[i]=5,arr2[j]=2,arr3[k]=5
            # 5==2==3 not same go to else block
            # step 3: i=1,j=1,k=0
            # 5==5==3 not same
            #step 4 : i=1j=1k=1 5==5==5 same so it will add 
            # step 5: i=2,j=2,k=2 20==20==20 then append it
            # add 5 value
            # add 20 value
            i+=1
            j+=1
            k+=1
            # move i=2,j=2,k=2
            # no index is there to increment
        else:
            minimum_val=min(arr1[i],arr2[j],arr3[k])
            #step1 : here 1==2==3 min value is 1 
            # step2 : here 5==2==3 min value is 2 so increment j value
            # step 3: here 5==5==3 min value is 3 so k increment
            if arr1[i]==minimum_val:
                i+=1
                # step1 here 1 increment in i value so arr1[i]=1
            elif arr2[j]==minimum_val:
                #step 2: minimun value is 2 j will increment  arr[j]=1
                j+=1
            else:
                k+=1
                # step 3: minimum is 3 k increment arr[k]=1
    return result
    # result is [5,20]

arr1=[1,5,20]
arr2=[2,5,20]
arr3=[3,5,20]
print(common_elements(arr1,arr2,arr3))

# Find leaders in an array
def leads(arr):
    n=len(arr)
    # len is  6 
    max_right=arr[-1] # chouse the arr of last element
    result=[max_right]
    for i in range(n-2,-1,-1): 
        # i=4 val =5 so 5>=2 yes [2,5]
        # i=3 val =3 5>= 3 no
        # i=2 val 4 5>=4 no
        # i=1 val 17 5>=17 true [2,5,17] 
        # i=0 val 16 17>=16 m0  
        if arr[i]>=max_right:
            max_right=arr[i]
            result.append(max_right)
            # res=[2,5,17]
    return result[::-1]
    # here reverse it [17,5,2]
arr=[16,17,4,3,5,2]
print(leads(arr))