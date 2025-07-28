import streamlit as st
import random

# --- Sudoku generation & puzzle functions ---

def generate_full_solution():
    board = [[0]*9 for _ in range(9)]
    def is_valid(num, pos):
        r, c = pos
        # Row check
        if any(board[r][i] == num for i in range(9)):
            return False
        # Column check
        if any(board[i][c] == num for i in range(9)):
            return False
        # 3x3 box check
        br, bc = (r//3)*3, (c//3)*3
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if board[i][j] == num:
                    return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(num, (i, j)):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = 0
                    return False
        return True

    solve()
    return board

def remove_numbers(full_board, difficulty):
    # Number of clues for each level
    clues_map = {"Easy": 36, "Medium": 32, "Hard": 28}
    clues = clues_map[difficulty]
    puzzle = [row[:] for row in full_board]
    cells_to_remove = 81 - clues
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    for i, j in positions[:cells_to_remove]:
        puzzle[i][j] = 0
    return puzzle

# --- Streamlit UI ---

st.set_page_config(page_title="Sudoku Puzzle", layout="wide")
st.title("🧩 Sudoku Puzzle Generator")

# Select difficulty
difficulty = st.selectbox("Choose difficulty", ["Easy", "Medium", "Hard"])

# Generate a new puzzle
if st.button("New Puzzle"):
    sol = generate_full_solution()
    st.session_state.solution = sol
    st.session_state.puzzle   = remove_numbers(sol, difficulty)
    # reset any previous inputs
    for i in range(9):
        for j in range(9):
            st.session_state[f"cell_{i}_{j}"] = ""

# Only show grid once puzzle exists
if "puzzle" in st.session_state:
    grid = st.session_state.puzzle
    sol  = st.session_state.solution

    st.write(f"**Difficulty:** {difficulty}")
    # Render 9×9 grid
    for i in range(9):
        cols = st.columns(9)
        for j, col in enumerate(cols):
            key = f"cell_{i}_{j}"
            if grid[i][j] != 0:
                # given clue
                col.number_input(
                    label="",
                    min_value=1, max_value=9,
                    value=grid[i][j],
                    key=key,
                    disabled=True,
                    label_visibility="hidden"
                )
            else:
                # user input
                col.text_input(
                    label="",
                    key=key,
                    max_chars=1,
                    label_visibility="hidden"
                )

    # Check solution
    if st.button("Check Solution"):
        filled = True
        correct = True
        for i in range(9):
            for j in range(9):
                val = st.session_state.get(f"cell_{i}_{j}", "").strip()
                if not (val.isdigit() and 1 <= int(val) <= 9):
                    filled = False
                elif int(val) != sol[i][j]:
                    correct = False
        if not filled:
            st.warning("🚨 Please fill in **all** empty cells before checking.")
        elif correct:
            st.success("🎉 Congratulations! You’ve solved it!")
        else:
            st.error("❌ There are mistakes. Keep trying!")
