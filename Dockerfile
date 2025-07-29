# 1. Base image with Python 3.12
FROM python:3.12-slim

# 2. Set working directory in container
WORKDIR /app

# 3. Copy over requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your application code
COPY . .

# 5. Expose the port Uvicorn will listen on
EXPOSE 8000

# 6. Command to launch your FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]