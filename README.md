# PyCODE Snippet API Documentation

## Base URL
```
https://api.py-code.in/
```

## Endpoints

### 1. Get All Routes
**Endpoint:**
```
GET /
```
**Description:**
Returns a list of all available API routes.

---
### 2. Get All Snippets
**Endpoint:**
```
GET /snippets/
```
**Description:**
Fetches all stored snippets.

**Response Example:**
```json
[
  {
    "id": "1234-uuid",
    "title": "Hello World",
    "code": "print('Hello World')",
    "lang": "Python",
    "created_at": "2024-03-17T12:34:56"
  }
]
```

---
### 3. Get a Specific Snippet
**Endpoint:**
```
GET /snippets/<id>
```
**Description:**
Fetches a snippet by its unique ID.

**Response Example:**
```json
{
  "id": "1234-uuid",
  "title": "Hello World",
  "code": "print('Hello World')",
  "lang": "Python",
  "created_at": "2024-03-17T12:34:56"
}
```

**Error Response:**
```json
{
  "error": "snippet not found"
}
```

---
### 4. Add a New Snippet
**Endpoint:**
```
POST /snippets/add
```
**Description:**
Adds a new snippet to the database.

**Request Example:**
```json
{
  "title": "New Snippet",
  "code": "print('Hello PyCODE')",
  "lang": "Python"
}
```

**Response Example:**
```json
{
  "status": 200,
  "msg": "New Snippet saved",
  "id": "5678-uuid"
}
```

---
### 5. Update an Existing Snippet
**Endpoint:**
```
PUT /snippets/update/<id>
```
**Description:**
Updates an existing snippet by ID.

**Request Example:**
```json
{
  "title": "Updated Snippet",
  "code": "print('Updated Code')",
  "lang": "Python"
}
```

**Response Example:**
```json
{
  "status": 200,
  "msg": "snippet updated!"
}
```

**Error Response:**
```json
{
  "error": "snippet not found!"
}
```

---
### 6. Delete a Snippet
**Endpoint:**
```
DELETE /snippets/delete/<id>
```
**Description:**
Deletes a snippet by ID.

**Response Example:**
```json
{
  "status": 200,
  "msg": "snippet deleted successfully!"
}
```

**Error Response:**
```json
{
  "error": "snippet not found!"
}
```