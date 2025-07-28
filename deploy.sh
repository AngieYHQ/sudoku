#!/usr/bin/env bash

# 1. Install/update pip
pip install --upgrade pip

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
