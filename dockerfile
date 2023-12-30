# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages
RUN pip install --no-cache-dir fastapi uvicorn pydantic
RUN pip install --no-cache-dir -q -U google-generativeai
RUN pip install --no-cache-dir IPython

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
