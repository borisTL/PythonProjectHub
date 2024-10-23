# [Sudoku Solver](https://github.com/borisTL/PythonProjectHub/blob/main/Sydoku_slover.py)


This project implements a backtracking algorithm to solve a Sudoku puzzle. The `Board` class represents the Sudoku board and includes methods to validate moves, find empty cells, and recursively solve the puzzle. The `solve_sudoku` function initializes the board and displays the puzzle before and after solving it.

## Features
- **Board Representation**: The board is represented as a 9x9 grid, where empty cells are denoted by `0`.
- **Validation Functions**: 
  - `valid_in_row`, `valid_in_col`, and `valid_in_square` ensure that each guess is valid based on the Sudoku rules.
- **Backtracking Solver**:
  - The solver uses a recursive backtracking approach to fill the board cell by cell, testing numbers from 1 to 9.
  - If an invalid guess is found, the solver backtracks and tries a new number.
- **Solver Output**: 
  - Displays the initial puzzle and the solved puzzle if a solution exists.
  - If the puzzle is unsolvable, the function will inform the user.
 ---
    
# [Budget Tracker](https://github.com/borisTL/PythonProjectHub/blob/main/Build%20a%20Budget%20App%20Project.py)
This project is a simple budget management system with spending categories. It includes a `Category` class that allows you to track deposits, withdrawals, and transfers >between categories. The project also features a function to create a chart displaying the distribution of spending.

 Features
 - **Spending Categories**: Add and track transactions (deposits, withdrawals, transfers) for each category.
 - **Spending Chart**: The `create_spend_chart` function generates a chart showing the percentage of spending in each category.
---
# [Shape Calculator](https://github.com/borisTL/PythonProjectHub/blob/main/Build%20a%20Polygon%20Area%20Calculator%20Project.py)


This project implements a simple shape calculator using Python. It includes two main classes: `Rectangle` and `Square`. The `Rectangle` class allows you to create and manipulate rectangles, while the `Square` class inherits from `Rectangle` but ensures that all sides are equal.

 Features
- **Rectangle Class**: Create a rectangle by specifying the width and height. Get the area, perimeter, and diagonal of the rectangle. Visualize the rectangle using the `get_picture()` method (limited to a maximum width or height of 50). Determine how many times one shape can fit inside another using the `get_amount_inside()` method.
- **Square Class**: Inherits from `Rectangle` and automatically ensures that both width and height are equal. Provides the same features as the `Rectangle` class, but with methods specifically for squares (e.g., `set_side()` to change both the width and height).

---
# [Hat Probability Experiment](https://github.com/borisTL/PythonProjectHub/blob/main/Build%20a%20Probability%20Calculator%20Project.py)

 Overview
This project simulates a probability experiment using a "hat" filled with balls of different colors. The `Hat` class allows drawing a specified number of balls, and the `experiment` function calculates the probability of drawing a certain combination of balls over multiple trials.

 Features
- **Hat Class**: 
  - Initialize with any number of colored balls.
  - `draw(num_balls)`: Draw a specified number of balls from the hat without replacement.
  
- **Experiment Function**:
  - Simulates drawing balls multiple times to estimate the probability of getting a specific combination of balls.
  - Returns the probability of success after running the specified number of experiments.

---
# [Time Calculator](https://github.com/borisTL/PythonProjectHub/blob/main/Build%20a%20Time%20Calculator%20Project.py)


This project implements a simple time calculator function, `add_time`, which takes a starting time and a duration, and calculates the resulting time, including the day of the week if provided. It correctly handles transitions between AM/PM and calculates how many days later the resulting time is.

 Features
- **Time Calculation**: Add a specified duration (in hours and minutes) to a given start time.
- **Day Calculation**: Optionally provide a starting day of the week, and the function will calculate the new day.
- **Correct Handling of AM/PM**: The function correctly handles the transition between AM and PM, including 12-hour clock conversion.
- **Day Transitions**: When the resulting time spans into the next day(s), the function outputs the number of days later or states `(next day)` if it's the next day.

---
# [Arithmetic Arranger](https://github.com/borisTL/PythonProjectHub/blob/main/Build%20an%20Arithmetic%20Formatter%20Project.py)


This project implements a function, `arithmetic_arranger`, which formats and arranges simple arithmetic problems (addition and subtraction) in vertical form, similar to how they would appear on paper. The function can optionally display the answers to the problems.

 Features
- **Input Validation**: 
  - The function supports only addition (`+`) and subtraction (`-`).
  - It handles up to 5 problems at a time and checks that the numbers are no longer than 4 digits.
  - The input must contain only digits and valid operators.
  
- **Formatted Output**: 
  - The function arranges the arithmetic problems vertically and aligns the numbers by their width.
  - Optionally, it can display the results of the calculations.

- **Error Handling**: 
  - The function returns an error if there are more than 5 problems or if any of the problems contain invalid operators, non-digit characters, or numbers longer than 4 digits.

---
# [Shortest Path Finder](https://github.com/borisTL/PythonProjectHub/blob/main/Shortest%20Path%20algorithm..py)


This project implements Dijkstra's algorithm to find the shortest path between nodes in a graph. The `shortest_path` function calculates the shortest distance from a starting node to a target node (or all nodes, if no specific target is given) in a weighted graph. The function also provides the actual path taken to reach the target node.

 Features
- **Graph Representation**: The graph is represented as a dictionary, where each key is a node, and the value is a list of tuples representing connected nodes and their respective weights.
- **Shortest Path Calculation**: 
  - Finds the shortest path from the start node to all other nodes or to a specific target node using Dijkstra’s algorithm.
  - Returns both the shortest distances and the paths taken to reach each node.
  
- **Flexible Output**: 
  - If no target node is specified, the function prints the shortest paths to all nodes.
  - If a target node is specified, it prints only the shortest path to that node.
---
# [Arithmetic Arranger](https://github.com/borisTL/PythonProjectHub/blob/main/arithmetic_arranger.py)

This project implements a function `arithmetic_arranger` that takes a list of arithmetic problems (in string format) and arranges them vertically for easier readability, similar to how they would appear in elementary math exercises. Optionally, the function can also display the results of the calculations.

 Features
- **Arrange Arithmetic Problems**: Formats up to 5 arithmetic problems (addition and subtraction) in vertical format.
- **Input Validation**:
  - Only supports addition (`+`) and subtraction (`-`) operations.
  - Numbers can only contain digits and must not exceed four digits in length.
  - Handles errors when more than 5 problems are provided or invalid input is detected.
---
# [Vector Operations with R2Vector and R3Vector](https://github.com/borisTL/PythonProjectHub/blob/main/building%20_vector_space..py)


This project implements two classes, `R2Vector` and `R3Vector`, to represent 2D and 3D vectors respectively. The classes support various vector operations, including addition, subtraction, scalar multiplication, dot product, and cross product (for 3D vectors).

 Features

- **R2Vector Class**:
  - Represents 2D vectors with `x` and `y` coordinates.
  - Supports basic vector operations such as:
    - Vector addition (`+`)
    - Vector subtraction (`-`)
    - Scalar multiplication and dot product (`*`)
    - Norm calculation (`norm`)
    - Comparisons (`==`, `<`, `>`, `<=`, `>=`)

- **R3Vector Class**:
  - Inherits from `R2Vector` and represents 3D vectors with an additional `z` coordinate.
  - Supports all operations of `R2Vector`, and also:
    - Cross product operation (`cross`).
---






