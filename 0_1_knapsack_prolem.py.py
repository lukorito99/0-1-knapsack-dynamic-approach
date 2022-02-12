'''
knapsack capacity j, 1 ≤ j ≤ W.

items, 1 ≤ i ≤ n, with weights w1 , . . . , wi, values v1, . . . , vi , and

Assumed that all weights and knapsack capacity,W are positive integers
Item values do not have to be integers

A recurrence relation is defined that expresses a solution to an instance of the problem in terms of solutions to its subinstances

Function knapsack(i,val,j) returns optimal solution to an instance;value of most valuable subset of first i items that fit into the knapsack of capacity j'''


def knapsack(i, val, j):
    #0/1 knapsack problem
    # Two subsets of first i items that fit into the knapsack;
    #    those that DO NOT include the ith item
    #    those that DO include the ith item

    # In those that do not include:
    #    value=knapsack(i-1,j)->optimal subset

    # In those that do include:
    #    hence (j-wi ≥ 0)
    #    value=ith item + optimal subset of first i-1 items fitting into capacity j-Wi
    #    so
    #    value=vi+knapsack(i-1,j-wi)->optimal subset

    # knapsack(i,val,j)={ max( knapsack (i − 1,val, j ), vi + knapsack (i − 1,val, j − wi) ) if j-wi >= 0
    #                 knapsack(i-1,val,j)  if j-wi < 0
    #               }
    #
    table = [[0 for a in range(j + 1)] for b in range(len(val) + 1)]

    # filling the table(memoization)
    for y in range(len(val) + 1):
        for z in range(j + 1):
            if y == 0 or z == 0:
                table[y][z] = 0
            elif i[y - 1] <= z:
                table[y][z] = max(val[y - 1]+ table[y - 1][z - i[y - 1]],
                              table[y - 1][z])
            else:
                table[y][z] = table[y - 1][z]

    # optimal solution is table[-1][-1]
    optimal_solution=table[len(val)][j]
    optimal_combo=[0 for a in range(len(val))]
    print(table)
    print('\nOptimal solution is:',optimal_solution,'\n')
    v=len(val)

    while v != 0:
        if table[v][j] != table[v-1][j]:
            optimal_combo[v-1]=1
            j-=i[v-1]
        v-=1

    return optimal_combo

weights= list()
values= list()

item_count=int(input('How many items are available?:\n'))
capacity=int(input('What is the capacity?:\n'))


for i in range(item_count):
    print('\nEnter weight for item:',i+1)
    weights.append(int(input('')))
    print('\nEnter the corresponding value for item:',i+1)
    values.append(float(input('')))

print('\nOptimal combination:',*knapsack(weights, values, capacity))
