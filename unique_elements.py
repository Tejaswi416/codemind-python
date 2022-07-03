def printDistinct(arr, n):
 
    # Pick all elements one by one
    for i in range(0, n):
 
        # Check if the picked element
        # is already printed
        d = 0
        for j in range(0, i):
            if (arr[i] == arr[j]):
                d = 1
                break
 
        # If not printed earlier,
        # then print it
        if (d == 0):
            print(arr[i],end=" ")
     
# Driver program to test above function
n=int(input())
arr=list(map(int,input().split()))[:n]
l=len(arr)
printDistinct(arr, l)