import os
import sys
import streamlit.web.cli as stcli

# Set working directory to the project root (important for config.toml)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "src/main.py"]
    sys.exit(stcli.main())