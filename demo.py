def ssort(arr):
    for i in range(0,len(arr)-1):
        min_pos = i 
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos],arr[i]    
        print(arr)


arr = []
n = int(input('enter the total number of element: '))
for i in range(n):
    x = int(input('enter the next value: '))
    arr.append(x)

ssort(arr)
print(arr)