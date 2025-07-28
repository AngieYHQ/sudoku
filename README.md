# Sudoku Puzzle Generator (with Graph Theory Inspiration)
________________________________________________________________________
This project is a simple web-based Sudoku puzzle generator built using Streamlit. It features 3 difficulty levels (Easy, Medium, and Hard) — and visually highlights puzzle numbers for better user experience.

🔧 Features
- Generate Sudoku puzzles with 3 difficulty levels
- Color-coded cells for better readability
  
# How to play?
- Game run on local machine, in your terminal:
- Step 1 Download package, in this page, go to the drop down arrow in green botton [Code] _> Download Zip file
- Step 2 Open you laptop file folder, extract the downlaoded zip and save
- Step 3 In this file location, right click find -> Open in terminal
- Step 4, do this
    copy and paste, run this ->pip install pygame
    copy and paste, run this ->pip install python
    copy and paste, run this ->copy and paste, run this -> python3 GUI.py
  Done!
________________________________________________________________________

🎯 Why I Built This
While exploring graph theory and tools like NetworkX, I came across the concept of graph coloring — a powerful technique used to solve constraint problems. Graph coloring forms the foundation for solving real-world challenges like:

- Scheduling and timetabling
- Frequency assignment (e.g., mobile networks)
- Wavelength routing
- Task allocation

To deepen my understanding of how graphs work — especially the breadth and depth of entity relationships — I wanted to apply this concept in a fun, hands-on way. Sudoku was the perfect candidate.
Even though this app uses backtracking (not NetworkX yet), it’s inspired by graph coloring, and it serves as my stepping stone to visualize and eventually model Sudoku puzzles using graph-based approaches.

🧠 What I Learned
-  Basics of graph coloring as a constraint satisfaction method
-  How Sudoku can be modeled as a graph with 81 nodes and conflict edges
-  Backtracking as a fundamental algorithm
-  Streamlit for rapid web prototyping
-  Visualizing data using colored HTML tables  

🚀 Future Plans
- Solve puzzles using graph coloring via NetworkX
- Let users input their own puzzle and validate it
- Add solving assistant and timer
________________________________________________________________________
  Scripts:
1️⃣ sudokuGenerator - script that generates a 9X9 sudoku board according to the sudoku puzzle rules - using the backtracking algorithm
2️⃣ sudokuSolverAlgo - script that solves the sudoku puzzle - using the backtracking algorithm
3️⃣ chooseLevel - simple script for the level difficulty GUI
4️⃣ GUI - the main script, the player runs this script to play the game
