# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables to non-interactive to avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository and install required tools
RUN apt-get update && \
    apt-get install -y \
    hydra \
    nmap \
    nikto \
    sqlmap \
    curl \
    wget \
    python3 \
    python3-pip \
    gnupg2 \
    git \
    sudo

# Install Metasploit-Framework from Rapid7 repository
RUN apt-get install -y gnupg2
RUN curl -fsSL https://apt.metasploit.com/metasploit-framework.gpg.key | sudo apt-key add -
RUN echo 'deb https://apt.metasploit.com/ jessie main' > /etc/apt/sources.list.d/metasploit-framework.list
RUN apt-get update && \
    apt-get install -y metasploit-framework

# Install Commix from GitHub repository
RUN git clone https://github.com/commixproject/commix.git /opt/commix
RUN ln -s /opt/commix/commix.py /usr/local/bin/commix

# Copy the hello.sh script into the container
COPY hello.sh /home/ubuntu/
RUN chmod +x /home/ubuntu/hello.sh

# Set the entrypoint to execute hello.sh
ENTRYPOINT ["/home/ubuntu/hello.sh"]
