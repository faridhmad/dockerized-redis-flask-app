# Simple Dockerized Flask-Redis Hit Counter

This project demonstrates a basic hit counter application built using Flask and Redis, containerized with Docker for easy deployment.

## Features

* **Hit Counter:** Counts the number of visits to the `/` endpoint using Redis as a persistent store.
* **Dockerized:** Includes a `Dockerfile` and `docker-compose.yml` for streamlined setup and execution within containers.
* **Graceful Error Handling:** Handles potential Redis connection issues with retries.

## How It Works

1. **Flask App (`app.py`)**:
   * Initializes a connection to a Redis instance.
   * The `/` route increments a counter in Redis and displays the current count to the user.
   * The `/health` route provides a simple way to check the health status of the Flask application and its connection to the Redis server.
2. **Docker Configuration:**
   * **`Dockerfile`:** Builds a Docker image containing the Flask application, its dependencies, and a production-ready WSGI server (Gunicorn).
   * **`compose.yml`:** Defines services for the Flask app and a Redis instance, managing their interaction and making it easy to start them together.

## How to Run (using Docker)

1. **Prerequisites:**
   * Docker and Docker Compose installed on your system.
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/faridhmad/dockerized-redis-flask-app.git
   ```
3. **Start the App:**
   ```bash
   docker-compose up --build
   ```
4. **Access the App:**
   Open your web browser and go to `http://localhost:8000`. You should see a message indicating how many times the page has been viewed. Refresh to see the counter increment.

## Project Structure

* `app.py`: Flask application code.
* `Dockerfile`: Instructions for building the Docker image.
* `docker-compose.yml`: Configuration for Docker Compose.
* `requirements.txt`: Python dependencies.

## Future Improvements

* **Environment Variables:** Store Redis connection details (host, port) in environment variables for better configuration management.
* **Persistent Volume:** Use a Docker volume to make the Redis data persistent even if the container is stopped or removed.
* **More Advanced Features:** Add user authentication, rate limiting, or a more visually appealing interface. 


## Contributing

Feel free to fork this repository and submit pull requests if you have ideas for enhancements or bug fixes.

## License

This project is open source. Feel free to use and modify it as you wish.
