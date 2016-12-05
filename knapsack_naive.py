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
W = 50
weight = [10, 20, 30]
value = [60, 100, 120]
n = len(value)

print "Naive recursive that return max value of knapsack of capacity W"
print "Max value: ", knapSack(W, weight, value, n)
    
