#naive representation of knapsack
def knapSack(W, weight, value, n):
    #base case
    if n == 0 or W == 0 :
        return 0

    #case if the weihgt in the nth item is more than knapsack of capacity
    #W, it cannot be included in optimal solution
    if (weight[n-1] > W ) :
        return knapSack (W, weight, value, n-1)

    #max of two cases
    else:
        return max(value[n-1] + knapSack(W-weight[n-1], weight, value, n-1), knapSack(W, weight, value, n-1))


### TEST ###
W = 10
weight = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
value = [5, 4, 3, 2, 1]
n = len(value)

print knapSack(W, weight, value, n)
    
