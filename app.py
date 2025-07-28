import streamlit as st
import pandas as pd
import time
from sudoku_generator import generate_full_solution, remove_numbers

st.set_page_config(page_title="Sudoku Generator", layout="wide")
st.title("🧩 Sudoku Puzzle Generator")

# Session state
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

difficulty = st.selectbox("Select difficulty level", ["Easy", "Medium", "Hard"])

if st.button("Generate Sudoku"):
    st.session_state.start_time = time.time()
    st.session_state.puzzle = remove_numbers(generate_full_solution(), difficulty)
    st.session_state.difficulty = difficulty

if "puzzle" in st.session_state:
    st.subheader(f"{st.session_state.difficulty} Puzzle")

   def render_colored_grid(grid):
    def cell_style(value, row, col):
        if value == 0:
            display = "."
            color = "#ccc"
            weight = "normal"
        else:
            display = value
            colors = {
                1: "#1f77b4", 2: "#ff7f0e", 3: "#2ca02c", 4: "#d62728", 5: "#9467bd",
                6: "#8c564b", 7: "#e377c2", 8: "#7f7f7f", 9: "#bcbd22"
            }
            color = colors[value]
            weight = "bold"

        border_style = "1px solid #ccc"
        if row % 3 == 0:
            top = "2px solid black"
        else:
            top = border_style
        if col % 3 == 0:
            left = "2px solid black"
        else:
            left = border_style

        return f'<td style="width: 40px; height: 40px; text-align: center; color: {color}; font-weight: {weight}; border-top: {top}; border-left: {left}; border-right: {border_style}; border-bottom: {border_style};">{display}</td>'

    html = '<table style="border-collapse: collapse;">'
    for i, row in enumerate(grid):
        html += "<tr>"
        for j, val in enumerate(row):
            html += cell_style(val, i, j)
        html += "</tr>"
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)


    render_colored_grid(st.session_state.puzzle)

    df = pd.DataFrame(st.session_state.puzzle)
    csv = df.to_csv(index=False, header=False)
    st.download_button("Download Puzzle CSV", data=csv, file_name="sudoku.csv", mime="text/csv")

    # Show timer
    if st.session_state.start_time:
        st.session_state.elapsed = int(time.time() - st.session_state.start_time)
        mins, secs = divmod(st.session_state.elapsed, 60)
        st.success(f"⏱ Time elapsed: {mins:02d}:{secs:02d}")

    # Submit button
    if st.button("Submit"):
        final_time = int(time.time() - st.session_state.start_time)
        mins, secs = divmod(final_time, 60)
        st.session_state.start_time = None
        st.success(f"🎉 Well done! You solved it in {mins:02d}:{secs:02d}")
        st.session_state.leaderboard.append({
            "Difficulty": st.session_state.difficulty,
            "Time (min:sec)": f"{mins:02d}:{secs:02d}"
        })

    # Show leaderboard
    if st.session_state.leaderboard:
        st.markdown("### 🏆 Leaderboard")
        st.dataframe(pd.DataFrame(st.session_state.leaderboard))
