FROM python:3.10-slim

WORKDIR /app

# Copy project files
COPY main.py .
COPY pyproject.toml .
COPY README.md .

# Install dependencies
RUN pip install --no-cache-dir pip -U && \
    pip install --no-cache-dir . && \
    pip install --no-cache-dir fastapi uvicorn

# Expose the port MCP server will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "main.py"]
