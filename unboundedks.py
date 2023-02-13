import numpy as np

""" 
Following function solves the unbounded knapsack problem using a bottom up dynanic
programming approach that incrementally solves horizontally for incremental capacity and vertically
for additoinal item types.  Accepts a list of (weight, profit) tuples and a maximum capacity and 
returns ??? WHAT REUTRN NOW. 
"""
def unboundedKS(weight_profit, max_capacity):
    #Cannot have negative capacity
    if(max_capacity < 0):
        return None

    print("in gunction")
    #unzip the (weight, profit tuples) for clarity
    weight, profit = zip(*weight_profit)

    #make a 2D array at width and height 1 greater than the max capacity and number of weights respectively
    knapsack_arr = [[0] * (max_capacity + 1) for i in range(len(weight) + 1)]
    table_w = len(knapsack_arr[0]) #table width (horizontal)
    table_h = len(knapsack_arr) #table height (vertical)

    #print(weight[0])

    #print(table_h, " ", table_w, "weight at 3", weight[3])
    #for 0 weight initialize row with 0
    #for i in range(table_w):
        #knapsack_arr[0][1] = 0

    #for i in range(table_h):
        #knapsack_arr[i][0] = 0

    #for each (weight, profit) 
    for i in range(table_h): #i is the item
        print('i = ', i)
        for j in range(table_w): #j is the capacity
            if (i == 0 or j == 0):
                #print('in i = 0')
                knapsack_arr[i][j] = 0 #initializing top row with 0 and all 0 capacity with 0
            else:
                #print('weight ', weight[i])
                print("i ", i, " j ", j)
                if(weight[i - 1] <= j): #if some multiple of the current item weight "fits" in the current capacity
                    #the highest knapsack value for the current capacity as of the previous item
                    prev_high = knapsack_arr[i - 1][j] 
                    #print(prev_high)
                    #the value of the current item + the highest previous value that has enough remaining
                    #capacity for the current item (value at capacity - current item weight)
                    candidate = profit[i - 1] + knapsack_arr[i][j - weight[i - 1]]
                    #print(candidate)
                    print('\n')
                    #whichever value is higher goes to the current cell in the matrix, representing the
                    #highest possible value for the knapsack for this subset of items at this capacity
                    if(candidate >= prev_high):
                        knapsack_arr[i][j] = candidate
                    else:
                        knapsack_arr[i][j] = prev_high
                else: #otherwise, the current item will not "fit" and we take the maximum value for this capacity
                    #as of the prior item
                    knapsack_arr[i][j] = knapsack_arr[i - 1][j]

    return knapsack_arr


    #for each item, 
    #for i in range

    print(weight);
    print(profit);

    print('done')

#temp hardcodes
#weight_profit = [(1, 2), (2, 5), (4, 8)]
weight_profit = [(1, 15), (3, 50), (4, 60), (5, 90)]
capacity = 8

result = unboundedKS(weight_profit, capacity)
#print(unboundedKS())
print(np.matrix(result))

