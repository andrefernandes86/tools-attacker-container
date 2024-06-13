# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables to non-interactive to avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository and install required tools
RUN apt-get update && \
    apt-get install -y \
    hydra \
    nmap \
    metasploit-framework \
    nikto \
    sqlmap \
    commix \
    curl \
    wget \
    python3 \
    python3-pip

# Clean up APT when done to reduce image size
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the entrypoint to bash for interactive use
ENTRYPOINT ["/bin/bash"]
