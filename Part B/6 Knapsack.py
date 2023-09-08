def knapsack_max_profit(weight,costs,capacity):
    num_items=len(weight)
    table=[[0]*(capacity+1) for _ in range(num_items+1)]
    for i in range(1,num_items+1):
        for j in range(1,capacity+1):
            if weight[i-1] <=j:
                table[i][j]=max(costs[i-1]+table[i-1][j-weight[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    selected_items = []
    total_weights = capacity
    for i in range(num_items,0,-1):
           if table[i] [total_weights] !=table[i-1][total_weights]:
              selected_items.append(i-1)
              total_weights -=weight[i-1]
    return table[num_items][capacity], selected_items 

weight = input("Enter the weights of the items (comma-separated): ")
weight = [int(w) for w in weight.split(",")]
costs = input("Enter the costs of the items (comma-separated): ")
costs = [int(c) for c in costs.split(",")]
capacity = int(input("Enter the capacity of the knapsack: "))

max_profit,selected_items=knapsack_max_profit(weight,costs,capacity) 
print("Maximum Profits: ",max_profit)
print("Selected Coffee Beans[index]:",selected_items)
print("Selected Coffee Beans[weight]:",[weight[i] for i in selected_items])
print("Selected Cofee Beans[costs]:",[costs[i] for i in selected_items]) 

'''
Enter the weights of the items (comma-separated): 2,3,4,5
Enter the costs of the items (comma-separated): 10,20,30,40
Enter the capacity of the knapsack: 10
Maximum Profits:  70
Selected Coffee Beans[index]: [3, 1, 0]
Selected Coffee Beans[weight]: [5, 3, 2]
Selected Cofee Beans[costs]: [40, 20, 10]
'''
   