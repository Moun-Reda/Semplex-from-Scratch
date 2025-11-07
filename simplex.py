import numpy as np
constraints_n=int(input("Enter number of constraints: "))
coofficients_n=int(input("Enter number of coefficients in objective function: "))
A=[] # coefficients matrix
B=[]# RHS vector
row=[]

# Input objective function coefficients
print("Enter the coefficients of the objective function:")
for i in range(coofficients_n):
    row.append(float(input(f"Enter coefficient X{i+1}: "))*-1)# times -1 for trasportation from rhs to lhs
row += [0] * constraints_n  # Initialize slack variable coefficients to 0
A.append(row)
B.append(0)  # Objective function RHS is 0


# Input constraints
for i in range(constraints_n): 
    row=[]#to add new row in each iteration
    print(f"Enter coefficients of constraint {i+1} in order aX1 + bX2 + ... <= c: ")    
    for j in range(coofficients_n):
        val=float(input(f"Enter coefficient X{j+1}: "))
        row.append(val)
    slack = [0] * constraints_n#to add slack variables 
    slack[i] = 1# to identify the slack variable for this constraint
    row += slack  # Add slack variable coefficients 
    rhs=float(input("Enter RHS value (c): "))
    B.append(rhs)
    A.append(row)

print("Rows in A:", len(A))
print("Entries in B:", len(B))

# Convert A and B to numpy arrays
A = np.array(A)
B = np.array(B)

# Build the tableau
tableau = np.hstack((A, B.reshape(-1, 1)))  # Combine A and B column-wise
print("\nInitial Tableau:\n", tableau)

while np.any(tableau[0, :-1] < 0):  # Check for negative values in objective row
    col = np.argmin(tableau[0, :-1])  # Choose column with most negative value
    pivot_column = tableau[1:, col]
    rhs_column = tableau[1:, -1]
    ratios = np.where(pivot_column > 0, rhs_column / pivot_column, np.inf) # Calculate ratios and if the the divisor is less than or equal to 0 set ratio to infinity   
    row = np.argmin(ratios) + 1  # Choose row with smallest positive ratio
    pivot_val = tableau[row, col]
    tableau[row] /= pivot_val  # Make pivot element equal to 1
    for r in range(len(tableau)):
        if r != row:
            tableau[r] -= tableau[r, col] * tableau[row]  # Zero out other entries in pivot column
print("\nFinal Tableau:\n", tableau)

 
# Extract solution
num_vars = coofficients_n + constraints_n  # total variables (original + slack)
solution = np.zeros(num_vars)

for col in range(num_vars):
    column = tableau[1:, col]  # skip objective row
    if list(column).count(1) == 1 and list(column).count(0) == constraints_n - 1:
        row_index = np.where(column == 1)[0][0] + 1  # +1 to skip objective row
        solution[col] = tableau[row_index, -1]  # RHS value

# Display results
print("\nBasic variable values:")
for i in range(coofficients_n):
    print(f"X{i+1} =", solution[i])
for i in range(constraints_n):
    print(f"Slack{i+1} =", solution[coofficients_n + i])
print("value of Z:", tableau[0, -1])
