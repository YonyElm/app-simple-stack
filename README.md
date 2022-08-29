# App Simple Stack

The idea behind this repository is to create a minimal and easily deployable architecture that doesn't depend on many framework or dependencies yet represent a modern application stack accurately.

The architecture includes
* Frontend - Based on NGINX, JS and HTML
* Backend - Based on Flask, and Python
* DB - Simple MySQL docker container

## Setup

### Local Environment

1. Instal Docker and Docker compose
2. Run `docker-compose build`
3. Run `docker-compose up`
4. Access to `http://localhost/index`

### AWS Environment

Follow these steps assuming an EC2 with public IP already exists

1. Run the following commands in EC2
    ```
    #!/bin/bash
    # Install Docker
    sudo yum install -y git
    sudo amazon-linux-extras install docker -y
    sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    # Download Lab files (git is preinstalled on machine)
    git clone https://github.com/YonyElm/app-simple-stack.git
    # Turn on docker
    sudo service docker start
    # Build and run container
    cd app-simple-stack
    sudo /usr/local/bin/docker-compose build
    sudo /usr/local/bin/docker-compose up
    ```
2. Access to `http://<ServerIP>/index`

## DB Access

The architecture doesn't connect to the MySQL DB automatically under the assumption that the DB may be handled separately in cloud environment.
Connection to the DB is done after architecture is running in `http://<ServerIP>/settings`
It's possible to choose between the existing MySQL container or an external MySQL server.When choosing the existing container provide the following credentials:
* HOST == "db"
* DB name == "example"
* Username == "user1"
* Password == "123456"
