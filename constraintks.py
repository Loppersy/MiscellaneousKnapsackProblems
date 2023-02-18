import anytree as at

"""
Recursively builds a tree whose leaf nodes are all possible subsets of the item pairs whose total weight
does not exceed the capacity of the knapsack. Returns the root node to the tree.  Each node contains a 
list of the item indexes that comprise that subset, the total weight, and the total profit.
"""


def kstree(weight_profit, max_capacity):
    root = at.AnyNode(subset=[], weight=0, profit=0)  # root node representing the empty set

    weight_list, profit = zip(*weight_profit)
    n = len(weight_list)  # grab the number of items

    # if the max capacity is greater than 0, build a tree out of possible item subsets
    if (n > 0):
        buildtree(0, n, max_capacity, weight_list, profit, root)

    return root


"""
Helper function builds the tree for the outer kstree function
"""


def buildtree(i, n, capacity, weight_list, profit, parent):
    # i corresponds with the indexes of the weights composing this subset
    if (i < n):
        # copy and append the index list for the right child
        rightset = []

        # make a copy of the current subset and append the index of the next item to it
        for j in parent.subset:
            rightset.append(j)
        rightset.append(i)

        # propagate the left (duplicate) leaf
        leftchild = at.AnyNode(subset=parent.subset, weight=parent.weight, profit=parent.profit, parent=parent)
        buildtree(i + 1, n, capacity, weight_list, profit, leftchild)

        # only add the current item to the right set if it doesn not put the total weight over
        # capacity, and calculate total profit for the current right itemset
        total_weight = parent.weight + weight_list[i]
        total_profit = parent.profit + profit[i]
        if (total_weight <= capacity):
            rightchild = at.AnyNode(subset=rightset, weight=total_weight, profit=total_profit, parent=parent)
            buildtree(i + 1, n, capacity, weight_list, profit, rightchild)


"""
Traverses a tree of itemset nodes and returns the item subset of the odd-weight leaf node with the highest even profit 
"""


def getmaxsubset(root):
    # initialize
    solution_set = None
    odd_weight = 0
    max_even_profit = 0

    for node in at.PreOrderIter(root):
        # if the current node has an odd weight and an even profit, may be a contender itemset for the max profit given
        # these constraints provided it is also a leaf node
        if (node.is_leaf and node.weight % 2 == 1 and node.profit % 2 == 0 and node.profit >= max_even_profit):
            max_even_profit = node.profit
            solution_set = node.subset
            odd_weight = node.weight

    return max_even_profit, odd_weight, solution_set


# weight_profit = [(2, 3), (3, 4), (4, 5)]
#
# capacity = 6
#
# tree_root = kstree(weight_profit, capacity)
# print(at.RenderTree(tree_root))  # prints tree
# max_profit, odd_weight, solution_set = getmaxsubset(tree_root)
#
# print("\n\nSOLUTION\nset ", solution_set, " with profit", max_profit, "and weight", odd_weight)
