import os
import sys
import streamlit.web.cli as stcli

# Set working directory to project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Check if we're running on Azure (has $PORT environment variable)
    port = os.getenv("PORT", "8501")  # Use 8501 locally if $PORT is not set

    # Use 'localhost' for local testing
    address = "localhost"

    # Prepare command arguments for Streamlit
    sys.argv = [
        "streamlit",
        "run",
        "src/main.py",
        "--server.port=" + port,  # Use the correct port based on $PORT or default to 8501
        "--server.address=" + address  # Set address to localhost for local dev
    ]

    sys.exit(stcli.main())