#!/bin/bash

ollama serve &

sleep 5

cd src/

streamlit run app.py --server.port 8501
