# docker_flask_homework

# Part 1: Dockerizing a Single Flask Application
## Setting Up

1. Created a flask app in my app.py file
2. Created a requirements.txt file for the packages I used in my flask app
3. Created a templates folder with an html file in it
4. Created a Dockerfile with the following lines:

```
FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```
## Interpreting Dockerfile 

- ```FROM python:3.7-alpine``` is a line that pulls a specific image from Dockerhub. In this case, the image "python:3.7-alpine" is being pulled.
- ```WORKDIR /app``` is a line that sets "/app" as the working directory
- ```COPY . /app``` is a line that takes all of the files in the directory and puts them into a virtual operating system / app called "app"
- ```RUN pip install -r requirements .txt``` is a line that installs everything inside the requirements.txt file
- ```EXPOSE 5000``` is a line thar exposes port 5000 to the operating system and allows it to communicate with the virtual system that Docker created
- ```CMD ["python", "app.py"]``` is a line that acts as a command to start the web app

## Build and Run Commands 
- Docker build command:
  ```docker build -t jess .```
- To see the images:
  ```docker images```
- Docker run command:
  ```docker run -d -p 5001:5000 jess```
- To display information about the Docker containers:
  ```docker ps```
- To stop the image from running:
  ```docker stop <container id>```
- To delete all images:
  ```docker system prune -a -f```

# Part 2: Multi-Container Setup with Docker Compose
## Setting Up
1. Created two folders for each of the flask applications titled "Flask1" and "Flask2" under a "Part 2" folder
2. In each folder, I created an app.py file the the flask application, a requirements.txt file for the packages used, a templates folder to hold the html file (if needed), an html file within the templates folder (if needed), and a Dockerfile
3. The Dockerfile in both of the folders has the following code:
   
```
FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```
4. Created a docker-compose.yaml file outside of the flask1 and flask 2 folders, but within the "Part 2" folder with the following lines:

```
version: '3'
services:
  flask_app_1:
    build: ./flask1
    ports:
      - "5003:5000"
    volumes:
      - ./flask1:/app
  flask_app_2:
    build: ./flask2
    ports:
      - "5002:5000"
    volumes:
      - ./flask2:/app
```

## Interpreting the docker-compose.yaml File
- version: the compose file version
- flask_app_1 / flask_app_2: name of the service
- services - build: path where the Dockerfile lies
- services - ports: expose ports
- services - volumes: changes made in flask1 / flask2 will automatically be pushed into the app folder inside the Docker folder

## Build and Run Commands
- Spinning up and running images command: docker-compose up --build
- Running Docker command: docker-compose up -d
- To see the apps Docker Compose created command: docker-compose ps
- Stop app command: docker-compose down

# Difference Between Docker vs. Docker Compose

The main difference I've noticed between Docker and Docker Compose is the ease of making new changes in the local environment and having it reflect in Docker / Docker Compose. Docker Compose establishes a link between a folder on a local machine and a folder in the virtual machine. In Part 1 with Docker, every time a change was made to any of the files, I had to rebuild the image because the new changes did not reflect onto Docker. I would have to re-rerun the Docker build and the Docker run command. However, with Docker compose, any changes that are made locally in any of the files are reflected automatically into Docker - I did not have to rebuild a new image and run additional code. Minor differences between Docker and Docker Compose are within the code itself. Some of the commands are different (ie: docker stop < container ID > vs. docker-compose down), but still have the same functionality.

# Challenges Faced

I faced one challenge when trying to do Part 2 of the assignment, but eventually resolved on my own because of human error. I had accidentally given the same port number for Part 2 Flask 1 and Part 1 of the assignment. When I was trying to run ```docker-compose up --build```, I kept running into an error message saying that my Dockerfile was empty. After I had changed the port number in Part 2 Flask 1, the error message disappeared and I was able to run my code successfully. 
