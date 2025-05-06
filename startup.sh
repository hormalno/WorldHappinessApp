#!/bin/bash
streamlit run src/main.py --server.port=$PORT --server.enableCORS=false
chmod +x startup.sh