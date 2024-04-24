# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY ass2.py .

# Copy the random_paragraphs.txt file into the container
COPY random_paragraphs.txt .

# Install NLTK and download stopwords
RUN pip install nltk matplotlib
RUN python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python", "ass2.py"] 