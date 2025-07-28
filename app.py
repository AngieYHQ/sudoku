import streamlit as st
import pandas as pd
from sudoku_generator import generate_full_solution, remove_numbers

st.set_page_config(page_title="Sudoku Generator", layout="wide")
st.title("🧩 Sudoku Puzzle Generator")

difficulty = st.selectbox("Select difficulty level", ["Easy", "Medium", "Hard"])
if st.button("Generate Sudoku"):
    full = generate_full_solution()
    puzzle = remove_numbers(full, difficulty)

    st.subheader(f"{difficulty} Puzzle")
    df = pd.DataFrame(puzzle)
    st.dataframe(df.style.set_properties(**{'text-align': 'center'}), height=400)

    csv = df.to_csv(index=False, header=False)
    st.download_button("Download Puzzle CSV", data=csv, file_name="sudoku.csv", mime="text/csv")
