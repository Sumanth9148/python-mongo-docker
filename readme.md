# Python MongoDB CLI App (Podman)

This project is a simple Python CLI application that stores user input into MongoDB and displays the data using Mongo Express.  
All services run in containers using Podman.



##  What this project does

- Accepts a name from the command line
- Stores the name in MongoDB
- Allows viewing stored data via Mongo Express UI
- Uses official MongoDB and Mongo Express images
- Uses a custom Python Docker image



##  Tech Stack

- Python 3.11
- MongoDB
- Mongo Express
- Podman
- podman-compose


##  How to Run
- Start MongoDB and Mongo Express
podman-compose up -d mongo mongo-express

- Run the Python CLI application
podman run --rm -it \
  --network python-mongo-podman_default \
  python-mongo-podman_app

- View data in Mongo Express

Open browser:

http://localhost:8081

- Stop the services
podman-compose down

- Data Persistence

MongoDB data is persisted using volumes and is not lost when containers stop.





