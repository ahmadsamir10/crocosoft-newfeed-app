
  

# Newsfeed App API

  

This is a simple Newsfeed API built using Flask-RESTful, with PostgreSQL as the database and Marshmallow for validation. It supports basic operations for managing users, posts, and interactions such as comments and likes.

  

---

  

## Table of Contents

  

1. [Project Description](#project-description)

2. [Features](#features)

3. [Technologies Used](#technologies-used)

4. [Installation](#installation)

5. [Development Guide](#development-guide)

6. [Project Structure](#project-structure)

7. [Entity-Relationship Diagram](#entity-relationship-diagram)

8. [API Documentation](#api-documentation)

9. [Contributing](#contributing)

  

---

  

## Project Description

  

The Newsfeed App API allows users to register, create posts, and interact with each other through comments, likes, and shares. This project follows REST principles and is designed to be scalable and easy to maintain.

  

## Features

  

- User registration and authentication

- Post creation, deletion, and updates

- Like, comment, and share posts

- Structured validation with Marshmallow

- API documentation in Swagger format

  

---

  

## Technologies Used

  

-  **Flask-RESTful**: For building RESTful APIs.

-  **PostgreSQL**: Relational database for storing user and post data.

-  **psycopg2**: PostgreSQL adapter for Python.

-  **Marshmallow**: For validating and serializing input data.

-  **dotenv**: For managing environment variables.

-  **Swagger**: API documentation.

  

---

  

## Installation

  

Follow the steps below to install and run the project on your local machine:

  

### Step 1: Clone the Repository

  

```bash

git clone https://github.com/ahmadsamir10/newsfeed-app.git

cd newsfeed-app

```

  

### Step 2: Create and Activate Virtual Environment

  

It's recommended to use a virtual environment for dependency management:

  

```bash

# Create a virtual environment

python3 -m venv venv

  

# Activate virtual environment (Linux/macOS)

source venv/bin/activate

  

# On Windows

venv\Scripts\activate

```

  

### Step 3: Install Dependencies

  

```bash

pip install -r requirements.txt

```

  

### Step 4: Set Up Environment Variables

  

Create a \`.env\` file at the root of the project with the following content:

  

```bash

DB_HOST=localhost

DB_NAME=newsfeed_app

DB_USER=your_postgres_user

DB_PASSWORD=your_postgres_password

DB_PORT=5432

```

  

Replace the values with your actual PostgreSQL database credentials.

  

### Step 5: Set Up the Database

  

Make sure PostgreSQL is installed and running. Then, create the database:

  

```bash

# Login to PostgreSQL

psql -U postgres

  

# Create the database

CREATE DATABASE newsfeed_app;

```

  

### Step 6: Run the SQL Script to Create Tables

  

Run the following Python script to create the required tables:

  

```bash
python create_tables_and_insert_data.py
```

  

This script will create tables and insert some sample data.

  

---

  

## Development Guide

  

### Running the Application

  

You can start the Flask server using the following command:

  

```bash
flask run
```

  

By default, the API will be accessible at \`http://localhost:5000\`.

  

  

---

  

## Project Structure

  

```

newsfeed_app/

│

├── .env # Environment variables for DB credentials

├── .gitignore # Git ignore file to exclude .env and other unnecessary files

├── app.py # Main entry point for the Flask app

├── config.py # Configuration file for DB connection using environment variables

├── db_connection.py # Database connection manager

├── query_builders/ # Folder for query builders

│ ├── __init__.py # Init file for query_builders module

│ └── post_query_builder.py # Query Builder class for Post entity

├── schemas/ # Folder for request body validation schemas

│ ├── __init__.py # Init file for schemas module

│ └── post_schema.py # Marshmallow schema for Post entity validation

├── resources/ # Folder for API resources (routes)

│ ├── __init__.py # Init file for resources module

│ └── post_resource.py # Resource for Post entity (CRUD operations)

├── requirements.txt # Python dependencies

├── swagger.json # Swagger documentation for the API

└── tables.sql # SQL script for creating tables

```

  

#### Main Components

  

-  **\`app.py\`**: The main entry point of the application.

-  **\`db_connection.py\`**: Manages database connections.

-  **\`query_builders/\`**: Contains query builders for each entity (e.g., \`PostQueryBuilder\` for posts).

-  **\`schemas/\`**: Defines input validation schemas (e.g., \`PostSchema\` for post validation).

-  **\`resources/\`**: Defines Flask-RESTful resources for handling API requests.

-  **\`swagger.json\`**: Swagger documentation for the API.

-  **\`tables.sql\`**: SQL file to create the required database tables.

  

---

  

## Entity-Relationship Diagram

  

The following is the Entity-Relationship Diagram (ERD) that shows the relationships between the main entities (User, Post, Comment, Like, Share, Friendship):

  

![ERD Diagram](https://www.plantuml.com/plantuml/png/lP9DIyD048Rl-okMd1J9HUWbb58GUj53GNekGpAIeViHToUjqlhVdIIMq2t6I_6IG9utyxpxiOmCWLjh53ec_jIRY44VbTOFL1MQ7ElvVFsyMCYNF9T7Azo1nKBl8PGrXBl7sUnUGXj7xotsGRH0PYhGG8m77whBZ80o831MM-12CrcKThPHN-hSRkqZJxKhlME9oi_umR_E6rQn7KUikX6ZvSbRY-uceaOAfwA_z2-qmmdtJLslild_9bi5GbV5cfefuvitnX-kvem44p9rR_hhV3hbkJzsbqTmDcHZTi5-ZbomXLqAkmCHOYWbm_O9Yl9EsRXQ2GpL9Q6w5jVM6eHrA746B97sU8Q9bgBkpLMcbk9ghVa6)

  

---

  

## API Documentation

  

You can find the API documentation in the \`swagger.yaml\` file. You can import this file into [Swagger Editor](https://editor.swagger.io/) to visualize and interact with the API.

  

The available endpoints are:

  

1.  **POST /posts** - Create a new post

2.  **GET /posts/{post_id}** - Get a post by ID

3.  **PUT /posts/{post_id}** - Update a post by ID

4.  **DELETE /posts/{post_id}** - Delete a post by ID