import streamlit as st
import numpy as np

st.set_page_config(page_title="Sudoku Solver", layout="wide")
st.title("🧩 Sudoku Puzzle")

# Initial puzzle from the image
puzzle = [
    [0, 2, 0, 7, 1, 0, 0, 0, 8],
    [0, 0, 1, 0, 9, 0, 6, 0, 0],
    [0, 6, 0, 5, 0, 0, 0, 9, 4],
    [3, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 1, 3, 6, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 5, 0],
    [2, 0, 4, 0, 7, 0, 3, 1, 0],
    [0, 7, 0, 0, 1, 0, 2, 0, 0],
    [0, 0, 6, 5, 0, 2, 0, 0, 7]
]

# Session state for editable grid
if "inputs" not in st.session_state:
    st.session_state.inputs = [[st.text_input("", str(puzzle[i][j]) if puzzle[i][j] != 0 else "", key=f"cell_{i}_{j}",
                                disabled=puzzle[i][j] != 0, max_chars=1) for j in range(9)] for i in range(9)]

# Display grid
st.subheader("Fill in the blank cells:")
for i in range(9):
    cols = st.columns(9)
    for j in range(9):
        cols[j].text_input("", st.session_state.inputs[i][j], key=f"cell_display_{i}_{j}",
                           disabled=True)

# Check solution button
if st.button("Check Solution"):
    def is_valid(board):
        for i in range(9):
            row = []
            col = []
            box = []
            for j in range(9):
                # Row
                r_val = board[i][j]
                if r_val in row and r_val != 0:
                    return False
                elif r_val != 0:
                    row.append(r_val)

                # Column
                c_val = board[j][i]
                if c_val in col and c_val != 0:
                    return False
                elif c_val != 0:
                    col.append(c_val)

                # Box
                r = 3 * (i // 3) + (j // 3)
                c = 3 * (i % 3) + (j % 3)
                b_val = board[r][c]
                if b_val in box and b_val != 0:
                    return False
                elif b_val != 0:
                    box.append(b_val)
        return True

    # Convert inputs to numbers
    current_board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = st.session_state[f"cell_{i}_{j}"]
            row.append(int(val) if val.isdigit() else 0)
        current_board.append(row)

    if is_valid(current_board):
        st.success("✅ The solution is valid so far!")
    else:
        st.error("❌ Invalid Sudoku solution. Check for duplicate numbers.")

