# Sudoku Puzzle Generator (with Graph Theory Inspiration)
________________________________________________________________________
This project is a simple web-based Sudoku puzzle generator built using Streamlit. It features 3 difficulty levels (Easy, Medium, and Hard) — and visually highlights puzzle numbers for better user experience.

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
  
🔧 Features
- Generate Sudoku puzzles with 3 difficulty levels
- Color-coded cells for better readability
- Simple, responsive UI via Streamlit

🚀 Future Plans
- Solve puzzles using graph coloring via NetworkX
- Let users input their own puzzle and validate it
- Add solving assistant and timer
