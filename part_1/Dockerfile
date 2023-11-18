FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

# FROM python:3.7-alpine is a line that pulls a specific image from Dockerhub. In this case, the image "python:3.7-alpine" is being pulled.
# WORKDIR /app is a line that sets "/app" as the working directory
# COPY . /app is a line that takes all of the files in the directory and puts them into a virtual operating system / app called "app"
# RUN pip install -r requirements .txt is a line that installs everything inside the requirements.txt file
# EXPOSE 5000 is a line thar exposes port 5000 to the operating system and allows it to communicate with the virtual system that Docker created
# CMD ["python", "app.py"] is a line that acts as a command to start the web app

# Docker build command: docker build -t jess .
# Docker images: to see the images
# Docker run command: docker run -d -p 5001:5000 jess
# Docker ps: displays information about the Docker containers
# Docker stop <container id> : to stop the image from running
# Docker system prune -a -f : delete all images