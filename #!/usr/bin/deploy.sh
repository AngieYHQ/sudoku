#!/usr/bin/env bash

# 1. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 2. Launch the app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
