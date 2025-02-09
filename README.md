### 1. Here's a basic **README.md** template for your `federated_learning` repository. You can modify it according to your specific project needs.

# Federated Learning

This repository contains code for a federated learning project that uses multiple Raspberry Pi devices in a distributed setting. The goal is to implement federated learning using Celery, Flower, and RabbitMQ on a Raspberry Pi 5 cluster. The repository includes the setup for the master and slave nodes, Docker configurations, and other necessary files to run federated learning workloads.

## Project Overview

Federated learning is a machine learning technique where multiple devices (clients) collaboratively train a model without sharing their data. Instead of sending the data to a central server, each client trains its local model and sends only the model updates (gradients) to the server.

This project aims to set up federated learning with the following components:
- **Master Node**: The server that coordinates the federated learning process.
- **Slave Nodes**: Raspberry Pi devices that participate in federated learning and send their model updates to the master node.
- **Celery**: A distributed task queue that runs tasks (model training) asynchronously.
- **Flower**: A real-time monitoring tool for Celery, providing insights into the progress of tasks.
- **RabbitMQ**: The message broker that manages communication between the master and slave nodes.

## Prerequisites

Before you begin, ensure you have the following installed:
- **Docker** and **Docker Compose** on all Raspberry Pi devices (both master and slaves).
- **Python 3.x** (for federated learning scripts).
- **Git** (for version control).

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine or Raspberry Pi:
```bash
git clone https://github.com/Bhumil1312/federated_learning.git
cd federated_learning
```

### 2. Build and Start Containers
To build and start the Docker containers for Celery, Flower, and RabbitMQ, use Docker Compose:
```bash
docker-compose up -d
```

This will set up:
- RabbitMQ as the message broker.
- Celery for task distribution.
- Flower for monitoring the Celery tasks.

### 3. Verify the Setup
- **Flower UI**: Access the Flower UI by navigating to `http://<master-ip>:5555` in a web browser.
- **Celery Tasks**: Check the status and logs of Celery tasks via Flower or Docker logs.

### 4. Running Federated Learning
Start the federated learning process by running the training scripts. The master node will coordinate the training, and the slave nodes will perform local training and send updates to the master.

## Usage

- **Master Node**: Run the server-side code that coordinates federated learning.
- **Slave Nodes**: Each Raspberry Pi device will run a local model and communicate with the master node.

### Example:
To start training on a slave node:
```bash
python train.py --slave
```

On the master node:
```bash
python train.py --master
```

## Contributing

Feel free to fork this project, create issues, and submit pull requests. Contributions are welcome!
