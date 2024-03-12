# Use a base image
FROM python:3.10.8-windowsservercore-1809

# Set the working directory
WORKDIR /app

# Copy the necessary files to the working directory
COPY . /app

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point command

RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf

CMD ["cmd", "/c", "echo Container started && python handler.py" ]