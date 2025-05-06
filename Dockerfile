# Use official Python image
FROM python:3.11-slim

# Environment variables for Streamlit
ENV PYTHONPATH="/app/src" \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ENABLECORS=false

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the full project (including src/)
COPY ./src /app/src

# Expose default Streamlit port
EXPOSE 8501

# Run Streamlit app located in src/
CMD ["streamlit", "run", "src/main.py"]