def printtable(arr):
    for row in arr:
        print(row)
    return

#items = [(3,2),(4,3),(5,4),(6,5)]
#W = 5

W = 10
items = [(2,2),(2,3),(6,5),(5,4),(4,6)]

arr = [[0 for _ in range(W+1)] for _ in range(len(items)+1)]

for i in range(1,len(items)+1,1):
    val,wt = items[i-1]
    for w in range(1,W+1,1):
        if wt <= w:
            arr[i][w] = max(arr[i-1][w] , val + arr[i-1][w-wt])
        else:
            arr[i][w] = arr[i-1][w]

printtable(arr)
