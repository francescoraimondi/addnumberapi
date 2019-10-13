# Necessary preamble :)
FROM ubuntu:18.10
LABEL maintainer="Francesco Raimondi <francesco.raimondi89@gmail.com>"

# Create local user
RUN apt update && apt install sudo -y && useradd -ms /bin/bash flaskuser && echo "flaskuser:flaskuser" | chpasswd && echo "flaskuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER flaskuser
WORKDIR /home/flaskuser

# Install  web server (nginx)
RUN sudo apt update && sudo apt install nginx -y

# Install necessary packages
RUN sudo apt update && sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv -y

# Prepare folder structure
COPY ./ ./flask-openapi
WORKDIR ./flask-openapi

# Install pip dependencies
RUN sudo -H pip3 install -r requirements.txt

# Update nginx conf 
RUN sudo cp ./nginx_default.conf /etc/nginx/sites-available/default 

# Start service
CMD sudo service nginx start && sudo uwsgi --ini flask_openapi.ini 
