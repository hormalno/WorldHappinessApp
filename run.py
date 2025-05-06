import os
import sys
import streamlit.web.cli as stcli

# Set working directory to project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Check if we're running on Azure (has $PORT environment variable)
    port = os.getenv("PORT", "8501")  # Default to 8501 locally

    # Use 'localhost' for local testing to avoid 0.0.0.0
    address = "localhost"  # Change from 0.0.0.0 to localhost

    # Prepare command arguments for Streamlit
    sys.argv = [
        "streamlit",
        "run",
        "src/main.py",
        "--server.port=" + port,  # Use Azure's port or default to 8501 locally
        "--server.address=" + address  # Set address to localhost for local dev
    ]

    sys.exit(stcli.main())