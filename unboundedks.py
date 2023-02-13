import numpy as np

""" 
Following function solves the unbounded knapsack problem using a bottom up dynanic
programming approach that incrementally solves horizontally for incremental capacity and vertically
for additoinal item types.  Accepts a list of (weight, profit) tuples and a maximum capacity and 
returns 2D knapsack solution matrix 
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

    #for each (weight, profit) 
    for i in range(table_h): #i - 1 is the item index
        print('i = ', i) #for each capacity [1...max capacity]
        for j in range(table_w): #j is the capacity
            #basecase handling
            if (i == 0 or j == 0):
                knapsack_arr[i][j] = 0 #initializing top row with 0 and all 0 capacity with 0
            else:
                if(weight[i - 1] <= j): #if some multiple of the current item weight "fits" in the current capacity
                    #the highest knapsack value for the current capacity as of the previous item
                    prev_high = knapsack_arr[i - 1][j] 
                    #the value of the current item + the highest previous value that has enough remaining
                    #capacity for the current item (value at capacity - current item weight)
                    candidate = profit[i - 1] + knapsack_arr[i][j - weight[i - 1]]
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

#temp hardcodes
weight_profit = [(1, 2), (2, 5), (4, 8)]

capacity = 6

result = unboundedKS(weight_profit, capacity)
print(np.matrix(result))