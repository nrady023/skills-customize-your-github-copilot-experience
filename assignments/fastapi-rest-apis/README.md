# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework so students can practice creating endpoints, handling requests, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create FastAPI Endpoints

#### Description
Set up a FastAPI application with several endpoints for creating, reading, updating, and deleting simple resources.

#### Requirements
Completed program should:

- Create a FastAPI app in `main.py` or a similar Python file.
- Define at least three endpoints using `@app.get()`, `@app.post()`, and `@app.put()` or `@app.delete()`.
- Return valid JSON responses using Python dictionaries.
- Test endpoints locally with the built-in FastAPI docs or HTTP requests.

### 🛠️ Use Request Data and Path Parameters

#### Description
Accept data from the client and use path parameters to identify resources.

#### Requirements
Completed program should:

- Accept JSON request bodies for `POST` or `PUT` requests.
- Use path parameters to retrieve or update a specific resource.
- Validate input with Pydantic models or simple Python checks.
- Return appropriate response data for each request.

### 🛠️ Handle API Responses and Errors

#### Description
Implement clear success and error responses for the API.

#### Requirements
Completed program should:

- Return HTTP status codes that match the request outcome.
- Provide success messages for completed operations.
- Return an error response if a requested resource is not found.
- Include a final example of how to run the API with `uvicorn`.
