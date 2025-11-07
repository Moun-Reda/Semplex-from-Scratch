# Simplex Method Solver in Python (Interactive CLI)

This project is a fully interactive Python implementation of the **Simplex algorithm** for solving linear programming problems. It is designed for **educational use**, oral defense, and collaborative learning — especially for students and instructors in **Operational Research** and **Intelligent Systems**.

---

## Features

- Interactive command-line input for:
  - Number of constraints and variables
  - Objective function coefficients
  - Constraint coefficients and RHS values
- Automatic construction of the Simplex tableau
- Safe pivoting logic with division-by-zero protection
- Extraction of basic variable values and optimal solution
- Bilingual-ready structure for teaching (English–Arabic)

---

## How It Works

1. **Input Phase**:
   - User enters the number of constraints and variables.
   - Objective function is entered and negated for maximization.
   - Slack variables are added automatically.
   - Constraints are entered one by one.

2. **Tableau Construction**:
   - Coefficient matrix `A` and RHS vector `B` are combined.
   - Slack variables form an identity matrix.

3. **Simplex Iteration**:
   - Pivot column is selected based on most negative coefficient.
   - Pivot row is chosen using safe ratio test.
   - Row operations are performed until optimality is reached.

4. **Solution Extraction**:
   - Basic variables are identified from identity columns.
   - Final values of decision and slack variables are printed.
   - Optimal value of Z is displayed.

---

## Requirements

- Python 3.x
- NumPy
