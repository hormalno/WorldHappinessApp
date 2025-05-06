import os
import sys
import streamlit.web.cli as stcli

# Set working directory to project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        "src/main.py",
        "--server.port=$PORT",  # Port Azure assigns
        "--server.address=0.0.0.0"  # Accessible to outside world
    ]
    sys.exit(stcli.main())