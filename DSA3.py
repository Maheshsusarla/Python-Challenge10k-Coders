#1 Search for an element using linear search

def liner_elament(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[10,20,30,40,50]
target=30
print(liner_elament(arr,target))


#2 Remove duplicates from a sorted array
class Soluction:
    def remove_element(self,num):
        k=0
        for i in range(1,len(num)):
            if num[k]!=num[i]:
                k+=1
                num[k]=num[i]
        return k+1
print(Soluction().remove_element([0,0,1,1,2,3,4,5]))