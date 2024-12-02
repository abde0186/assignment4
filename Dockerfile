FROM python:3.9

# Copy your Python script into the container
COPY A4_Yousef_Abdelaziz.py .

# Install required libraries
RUN pip install requests

# Command to run the Python script
CMD ["python", "A4_Yousef_Abdelaziz.py"]
