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

def unboundedtraceback(weight_profit, knapsack_arr):
    #unzip the (weight, profit tuples) for clarity
    weight, profit = zip(*weight_profit)

    table_w = len(knapsack_arr[0]) #table width (horizontal)
    table_h = len(knapsack_arr) #table height (vertical)
    
    count = [0] * (table_h - 1) #holds the count for the number of times each item has been added

    i = table_h - 1 #representative of the current item, starting from the end
    j = table_w - 1 #representative of the currend capacity, starting with the greatest

    #as long as we are not on the basecase of 0 items or capacity 0, continue matrix traceback
    while(knapsack_arr[i][j]): 
        #if the current cell is the same as the one above it, the current item has not been
        #added to the knapsack for this total capacity, so change to the previous item
        if(knapsack_arr[i][j] == knapsack_arr[i - 1][j]):
            i -= 1 #decrement i to get the previous item
        else:
        #otherwise the current item has been added to the knapsack, increment it's count
        #and go the the nearest horizontal cell less the current items' weight to see if
        #it has been added again
            count[i - 1] += 1 #increment the count for the current item
            j = j - weight[i - 1] #move horizontally backwards by the weight of this item
    
    return count


#temp hardcodes
weight_profit = [(1, 2), (2, 5), (4, 8)]

capacity = 6

result = unboundedKS(weight_profit, capacity)
print(np.matrix(result))

count = unboundedtraceback(weight_profit, result)
for i in range(len(weight_profit)):
    #if the count is >0 the corresponging i item has been selected
    if(count[i] > 0):
        print("Item ", weight_profit[i], " count ", count[i])