# MiscellaneousKnapsackProblems
This is group assignment done for an Artificial Intelligence class.

By Marcus Jessen Harms-Robinson, Sebastian Lopez Figueroa & Slade Ross

## Description
This program solves the following knapsack problems:
- 1-0 knapsack problem
- General knapsack problem
- Constraint knapsack problem (find the best solution with odd weight and even value)

The program uses a dynamic programming approach to solve the 1-0 knapsack problem and the general knapsack problem. The program uses a branch and bound approach to solve the constraint knapsack problem.

## To run the program
Run 'unboundedks.py'

You may need to install the following packages:
- numpy
- anytree

## Once running...
The program will ask you to input the following:
- data file name
- test number

The data file should be in the same directory as the program. The test number is the number of the test you want to run. The test numbers are as follows:
- 1: 1-0 knapsack problem
- 2: General knapsack problem
- 3: Constraint knapsack problem (find the best solution with odd weight and even value)
- 4: All of the above

## Data files
The data files contain the maximum weight of the knapsack, and the weight and value of each item. The data files are in the following format:
```
max weight
1 weight value
2 weight value
3 weight value
...
```

See SampleKnapsackData.txt for an example.

## Output
The program will output the following to the console:
- The maximum value of the knapsack
- The IDs of the items in the knapsack (line number in the data file)

Additionally, the program will output the following to a file named "DynamicTable.txt":
- The knapsack matrix for tests 1 and 2 and the search tree for test 3

## References
Our tall and handsome professor, Terry.