# 📘 Assignment: Standard Library Web APIs

## 🎯 Objective

Build a simple REST-style web API using Python’s standard library so students can practice HTTP request handling, JSON input/output, and server logic without external frameworks.

## 📝 Tasks

### 🛠️ Start a Basic HTTP Server

#### Description
Create a simple HTTP server that listens for incoming requests and responds with JSON data.

#### Requirements
Completed program should:

- Use `http.server` and `HTTPServer` to create the server.
- Send JSON responses with the appropriate `Content-Type` header.
- Run on a local port such as `8000`.

### 🛠️ Handle GET Requests and Path Parameters

#### Description
Support GET requests to list available items and fetch a single item by ID.

#### Requirements
Completed program should:

- Return a list of items when calling `/items`.
- Return a single item when calling `/items/{id}`.
- Respond with a 404 error if the requested item does not exist.

### 🛠️ Accept JSON POST Requests

#### Description
Allow the client to create new items by sending JSON data in a POST request.

#### Requirements
Completed program should:

- Read and parse JSON request bodies for `POST /items`.
- Add the new item to an in-memory list.
- Return a success response with the created item.
- Handle invalid JSON or missing fields gracefully.
