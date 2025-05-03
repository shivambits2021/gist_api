
<div align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=ffdd54" alt="Python">
    </a>
    <a href="https://fastapi.tiangolo.com/">
        <img src="https://img.shields.io/badge/FastAPI-005571?logo=fastapi" alt="Fastapi">
    </a>
    <a href="https://github.com/docker">
        <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker">
    </a>
</div>

<br/>

# 🛒 Backend System to GET GIST

A robust backend service for fetching gists from GitHub API. This service allows users to fetch a list of gists associated with a specific GitHub username.

## ⚙️ Requirements

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- Docker (for containerized environment)

## 🔌 Run Locally

### Prerequisite Installations

- Python 3.9 or higher
- Virtual environment (venv)

### Steps to Run Locally

1. **Clone the project**:

```bash
git clone https://github.com/shivambits2021/gist_api.git
```

2. **Create a virtual environment**:

```bash
virtualenv venv
```

3. **Activate the virtual environment**:

   - On Linux/macOS:

   ```bash
   source venv/bin/activate
   ```

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies**:

```bash
pip install -r requirements.txt
```

5. **Start the server**:

```bash
uvicorn app.main:app
```

   The server should be running at `http://localhost:8000`.

---

## 🐳 Run in Docker

If you prefer to run the application in a Docker container, follow these steps:

### Steps to Run in Docker

1. **Build the Docker image**:

   In the project root directory (where your Dockerfile is located), run the following command to build the Docker image:

```bash
docker build -t my-fastapi-app .
```

2. **Run the Docker container**:

   After the image is built, run the container with the following command:

```bash
docker run -p 8000:8000 my-fastapi-app
```

   This will run the FastAPI app in Docker and map port `8000` of the container to port `8000` on your local machine. You can access the app at `http://localhost:8000`.

   If port `8000` is already in use on your local machine, you can change the local port by modifying the command as follows:

```bash
docker run -p 8080:8000 my-fastapi-app
```

Now the app will be accessible at `http://localhost:8080`.

---

## 🛠️ Testing

To run the test suite, make sure you have installed the dependencies and then run the following command:

```bash
pytest
```

---

## 👷 Author

- [Shivam Pratap](https://www.linkedin.com/in/shivam-p-64a17615a)

---
