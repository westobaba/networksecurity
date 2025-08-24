# Change the base image to a supported Debian version
FROM python:3.10-slim-bullseye

WORKDIR /app
COPY . /app

# The apt-get commands will now work successfully
RUN apt-get update -y && apt-get install -y awscli

# Install Python dependencies
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]