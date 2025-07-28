import streamlit as st
import pandas as pd
import time
from sudoku_generator import generate_full_solution, remove_numbers, solve
import copy

st.set_page_config(page_title="Sudoku Generator", layout="wide")
st.title("🧩 Sudoku Puzzle Generator")

# Session state
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []
if "user_grid" not in st.session_state:
    st.session_state.user_grid = []

difficulty = st.selectbox("Select difficulty level", ["Easy", "Medium", "Hard"])

if st.button("Generate Sudoku"):
    st.session_state.start_time = time.time()
    full_solution = generate_full_solution()
    puzzle = remove_numbers(copy.deepcopy(full_solution), difficulty)
    st.session_state.solution = full_solution
    st.session_state.puzzle = puzzle
    st.session_state.difficulty = difficulty
    st.session_state.user_grid = [[puzzle[i][j] if puzzle[i][j] != 0 else "" for j in range(9)] for i in range(9)]

if "puzzle" in st.session_state:
    st.subheader(f"{st.session_state.difficulty} Puzzle (Enter your answers)")

    edited_grid = []

    for i in range(9):
        cols = st.columns(9)
        row = []
        for j in range(9):
            if st.session_state.puzzle[i][j] != 0:
                cols[j].markdown(f"<div style='text-align: center; font-weight: bold; font-size: 20px; padding: 10px; border: 1px solid #ccc; background-color: #f0f0f0;'>{st.session_state.puzzle[i][j]}</div>", unsafe_allow_html=True)
                row.append(st.session_state.puzzle[i][j])
            else:
                key = f"cell_{i}_{j}"
                value = cols[j].number_input("", min_value=1, max_value=9, value=int(st.session_state.user_grid[i][j]) if st.session_state.user_grid[i][j] != "" else 1, key=key)
                row.append(value)
        edited_grid.append(row)

    # Show timer
    if st.session_state.start_time:
        st.session_state.elapsed = int(time.time() - st.session_state.start_time)
        mins, secs = divmod(st.session_state.elapsed, 60)
        st.success(f"⏱ Time elapsed: {mins:02d}:{secs:02d}")

    if st.button("Submit"):
        st.session_state.start_time = None
        correct = st.session_state.solution
        user_correct = edited_grid == correct
        mins, secs = divmod(st.session_state.elapsed, 60)

        if user_correct:
            st.success(f"🎉 Well done! You solved it correctly in {mins:02d}:{secs:02d}")
        else:
            st.error("❌ Some answers are incorrect. Keep trying!")

        st.session_state.leaderboard.append({
            "Difficulty": st.session_state.difficulty,
            "Time (min:sec)": f"{mins:02d}:{secs:02d}",
            "Solved": "Yes" if user_correct else "No"
        })

    # Show leaderboard
    if st.session_state.leaderboard:
        st.markdown("### 🏆 Leaderboard")
        st.dataframe(pd.DataFrame(st.session_state.leaderboard))
