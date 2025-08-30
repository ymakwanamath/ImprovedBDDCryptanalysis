from pyeda import *
from pyeda.inter import *
import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np
# We first make bdds of each equation and then find solution by intersection. But there will be difference in the order of intersection.


for i in range(80):
    exec("x{}=exprvar('x',{})".format(i,i))





def Intersection_Sol(list1, list2):
    solutionset = list()
    for i in range(len(list1)):

        for j in list2:

            tempsol = dict(list1[i])

            check = True
            for x in tempsol.keys():
                if (x in j.keys()):
                    check = (tempsol[x] == j[x])
                    if (not check):
                        break

            if check:
                for x in j.keys():
                    tempsol.update({x: j[x]})

                solutionset.append(tempsol)
    return solutionset


def RSANDSoln(bdd_list2):
    #print(bdd_list2)
    m = len(bdd_list2)
    #print("len is", m)
    if (m == 1):
        return bdd_list2[0]
        #print("m=1 ")
        #print("output value is")
        #print(bdd_list2)
       
        
    else:
        m1 = math.floor((m+1)/2)
        #print("m1 is ", m1)

        bddlist1 = list()
        for i in range(m1-1):
            bddlist1.append(Intersection_Sol(bdd_list2[i],  bdd_list2[m-i-1]))

        if (m % 2) == 1:
            bddlist1.append(bdd_list2[m1-1])
        else:
            bddlist1.append(Intersection_Sol(bdd_list2[m1-1] , bdd_list2[m1]))
        #print(bddlist1)
        return(RSANDSoln(bddlist1))

def Sequential_intersection(solution_list):
    solution_set1 = list(sol_list[0])
    #print(sol_set)
    for index in range(len(solution_list)-1):
        solution_set1 = Intersection_Sol(solution_set1, solution_list[index+1])
    return solution_set1

def add_sequence_in_order(solution_list):
    n=len(solution_list)
    k=random.randint(1,n)
    # Step 2: Divide the sequence into subsets
    subsets = [solution_list[i:i + k] for i in range(0, n, k)]
    
    # Step 3: Add numbers within each subset
    subset_sums = [Sequential_intersection(subset) for subset in subsets]
    
    # Step 4: Add the sums of all subsets
    total_sum = Sequential_intersection(subset_sums)
    
    return total_sum

# Example usage




def Random_intersection(solution_list):


    n = len(solution_list) # Replace 10 with your desired number
    sequence = list(range(n))  # Create a list of numbers from 1 to n
    random.shuffle(sequence)  # Shuffle the list in place

    #print(sequence)  # Print the shuffled sequence
    solution=solution_list[sequence[0]]
    for i in range(n-1):
        solution=Intersection_Sol(solution, solution_list[sequence[i+1]])
    #print(solution)



def RSANDbdd(bdd_list):
    #print(bdd_list2)
    m = len(bdd_list)
    #print("len is", m)
    if (m == 1):
        return bdd_list[0]
        #print("m=1 ")
        #print("output value is")
        #print(bdd_list2)
       
        
    else:
        m1 = math.floor((m+1)/2)
        #print("m1 is ", m1)

        bddlist1 = list()
        for i in range(m1-1):
            bddlist1.append(bdd_list[i]&  bdd_list[m-i-1])

        if (m % 2) == 1:
            bddlist1.append(bdd_list[m1-1])
        else:
            bddlist1.append((bdd_list[m1-1] & bdd_list[m1]))
        #print(bddlist1)
        return(RSANDbdd(bddlist1))



#write all equations here.
eqn_list=[x0&x1 ^ x2&x3, x1&x2 ^ x3&x4, x3&x1+x2]


# Collecting equations in a single array
# Collecting equations in a single array

#Formation to bdd is here. 

bdd_list = list()
for i in range(len(eqn_list)):
    bdd_list.append(expr2bdd(eqn_list[i]))

#Initialize solution list. 

sol_list = list()
#Find all solutions to each bdd. 

for i in range(len(bdd_list)):
    sol_list.append(list(bdd_list[i].satisfy_all()))
#print("solution list is")
#print(sol_list)



#sol_set1 = list(sol_list[0])
#print(sol_set)
#for index in range(len(sol_list)-1):
    #sol_set1 = Intersection_Sol(sol_set1, sol_list[index+1])
#print("solution by direct intersection is")
#print(sol_set1)

#print("solution printed")
#print(RSANDSoln(sol_list))
#print("sol_set is")
#print(sol_set)

#Random_intersection(sol_list)

#Sequential_intersection(sol_list)


##########----- Time Calculation--------#########
#1) Sequential Intersection. 

start_sequential=time.time()
Sequential_intersection(sol_list)
end_sequential=time.time()

start_Random_intersection=time.time()
Random_intersection(sol_list)
end_Random_intersection=time.time()

start_RSAND=time.time()
RSANDSoln(sol_list)
end_RSAND=time.time()


#eqnarray to be defined. 


print("Time taken by sequential intersection is")
print(end_sequential-start_sequential)

print("Time taken by Random intersection is")
print(end_Random_intersection-start_Random_intersection)

print("Time taken by Recursive symmetric intersection is")
print(end_RSAND-start_RSAND)

eqn_array=[]

Time_taken_array=list()
for i in range(len(eqn_array)):
    print("for iteration ", i)
    eqn_list=eqn_array[i]
    start_bdd_anding=time.time()
    bdd_list = list()
    for i in range(len(eqn_list)):
        bdd_list.append(expr2bdd(eqn_list[i]))
    
    final_bdd= RSANDbdd(bdd_list)
    solution=final_bdd.satisfy_all()
    end_bdd_anding=time.time()
    #final_bdd=RSANDbdd(bdd_list)
    #solution_bdd=final_bdd.satisfy_all()
##########################################################################################################################   
    start_sequential=time.time()



    bdd_list = list()
    for i in range(len(eqn_list)):
        bdd_list.append(expr2bdd(eqn_list[i]))
    sol1=list(bdd_list[0].satisfy_all())
    for i in range(len(bdd_list)-1):
        sol=Intersection_Sol(sol1, bdd_list[i+1].satisfy_all())
    end_sequential=time.time()
    '''
    sol_list = list()
    for i in range(len(bdd_list)):
        sol_list.append(list(bdd_list[i].satisfy_all()))
    #Find all solutions to each bdd. 
    Sequential_intersection(sol_list)
    '''
    
#################################################################################################################
    start_Random_intersection=time.time()


    bdd_list = list()
    for i in range(len(eqn_list)):
        bdd_list.append(expr2bdd(eqn_list[i]))



    sol_list = list()
    #Find all solutions to each bdd. 

    for i in range(len(bdd_list)):
        sol_list.append(list(bdd_list[i].satisfy_all()))
    Random_intersection(sol_list)
    end_Random_intersection=time.time()
############################################################################################################
    start_RSAND=time.time()


    bdd_list = list()
    for i in range(len(eqn_list)):
        bdd_list.append(expr2bdd(eqn_list[i]))



    sol_list = list()
    #Find all solutions to each bdd. 
    for i in range(len(bdd_list)):
        sol_list.append(list(bdd_list[i].satisfy_all()))
    RSANDSoln(sol_list)
    end_RSAND=time.time()
####################################################################################################
    start_in_order=time.time()


    bdd_list = list()
    for i in range(len(eqn_list)):
        bdd_list.append(expr2bdd(eqn_list[i]))



    sol_list = list()
    #Find all solutions to each bdd. 
    for i in range(len(bdd_list)):
        sol_list.append(list(bdd_list[i].satisfy_all()))
    add_sequence_in_order(sol_list)
    end_in_order=time.time()

##########################################################################################################33

    print("Time taken by sequential intersection is")
    time_sequential=end_sequential-start_sequential
    print(time_sequential)

    print("Time taken by Random intersection is")
    time_Random_intersection=end_Random_intersection-start_Random_intersection
    print(time_Random_intersection)

    print("Time taken by Recursive symmetric intersection is")
    time_Recursive_symmetric=end_RSAND-start_RSAND
    print(time_Recursive_symmetric)

    print('time taken by bdd_anding like harish sahu paper is ')
    time_bdd_anding=end_bdd_anding-start_bdd_anding
    print(time_bdd_anding)

    print("time taken by intersection in order")
    time_intersection_in_order=end_in_order-start_in_order
    print(time_intersection_in_order)
    # Data to plot
    
    #time_taken_in_iteration=[time_sequential, time_Random_intersection, time_Recursive_symmetric, time_bdd_anding, time_intersection_in_order]
    #Time_taken_array.append(time_taken_in_iteration)
    # Data to plot
    #values = [time_taken_in_iteration]  # Replace these with your own values
    #labels = ['sequential, random, recursive, bdd_anding, in order']  # Labels for the bars

    # Create a figure and axis with a sleek aspect ratio
    #fig, ax = plt.subplots(figsize=(8, 5))

    # Use a well-balanced color palette
    #colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Blue, Orange, Green, Red

    # Create the bar graph with edge color for a sharp appearance
    #bars = ax.bar(labels, values, color=colors, edgecolor='black', linewidth=1.2)

    # Add data labels on top of each bar with a smaller, subtle font
    #for bar in bars:
        #yval = bar.get_height()
        #ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval}', 
                #ha='center', va='bottom', fontsize=10, color='#2C3E50', fontweight='medium')

    # Add a minimalist title and axis labels with consistent font
    #ax.set_title('Aesthetic Bar Graph of Values', fontsize=16, fontweight='bold', pad=15, color='#2C3E50')
    #ax.set_xlabel('Categories', fontsize=13, fontweight='medium', labelpad=10, color='#2C3E50')
    #ax.set_ylabel('Values', fontsize=13, fontweight='medium', labelpad=10, color='#2C3E50')

    # Customize the grid to be subtle and non-intrusive
    #ax.grid(True, which='major', axis='y', linestyle='--', linewidth=0.6, alpha=0.5)
    #ax.set_axisbelow(True)

    # Remove unnecessary spines and add a slight border to remaining ones
    #ax.spines['top'].set_visible(False)
    #ax.spines['right'].set_visible(False)
    #ax.spines['left'].set_linewidth(0.8)
    #ax.spines['bottom'].set_linewidth(0.8)

    # Set background to white for clarity in print and digital formats
    #ax.set_facecolor('#FFFFFF')

    # Apply tight layout for balanced spacing
    #plt.tight_layout()

    # Show the plot
    #plt.show()
















    #values = [time_Random_intersection, time_sequential, time_Recursive_symmetric, time_bdd_anding]  # Replace these with your own values
    #labels = ['random intersection', 'sequential', 'recursive', 'bdd_anding']  # Labels for the bars

    # Create a bar graph 
    #plt.bar(labels, values, color=['blue', 'green', 'red','yellow'])

    # Add title and labels
    #plt.title('Bar Graph of 3 Values')
    #plt.xlabel('Categories')
    #plt.ylabel('Values')

    # Show the plot
    #plt.show()

# Sample data: Replace with your actual data
data = np.array(Time_taken_array)

# Labels for the groups and setups
group_labels = ['time_sequential', 'time_Random_intersection', 'time_Recursive_symmetric', 'time_bdd_anding', 'time_intersection_in_order']
setup_labels = ['Setup 1', 'Setup 2', 'Setup 3', 'Setup 4']

num_setups = data.shape[0]

# Create subplots: 1 row, 4 columns
fig, axes = plt.subplots(1, num_setups, figsize=(16, 5), sharey=True)

# Plot each setup in its own subplot
for i in range(num_setups):
    axes[i].bar(group_labels, data[i], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
    axes[i].set_title(setup_labels[i], fontsize=14, fontweight='bold')
    axes[i].set_xlabel('Values', fontsize=12)
    axes[i].set_ylim(0, np.max(data))  # Ensure all bars are on the same scale
    for j, value in enumerate(data[i]):
        axes[i].text(j, value + 0.5, f'{value}', ha='center', fontsize=10, color='#2C3E50', fontweight='medium')

# Set a common ylabel
axes[0].set_ylabel('Measurements', fontsize=12)

# Add a tight layout
plt.tight_layout()

# Show the plot
plt.show()