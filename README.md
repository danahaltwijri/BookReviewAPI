# 📚 Book Review API

A backend web application developed using Django REST Framework that allows users to explore books, write reviews, and manage their accounts securely using JWT authentication.

---

# ✨ Main Features

* User account registration
* Secure login using JWT tokens
* Browse all available books
* View detailed information about each book
* Add reviews and ratings to books
* Edit or remove personal reviews
* Change account password
* Authentication and permission handling
* Admin control for managing books

---

# 🛠 Technologies and Tools

* Python
* Django
* Django REST Framework (DRF)
* Simple JWT Authentication
* SQLite Database
* Bootstrap 5

---

# ⚙️ Project Setup

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/BookReviewAPI.git
```

```bash
cd BookReviewAPI
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Apply Database Migrations

```bash
python manage.py migrate
```

---

## Create Admin User

```bash
python manage.py createsuperuser
```

---

## Run the Development Server

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Authentication System

This API uses JSON Web Tokens (JWT) for secure authentication through the `SimpleJWT` package.

## Obtain Access Token

### Endpoint

```text
POST /api/token/
```

### Example Request

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

---

# 📌 API Endpoints

## User Registration

```text
POST /api/register/
```

### Request Body

```json
{
    "username": "danah",
    "password": "12345678"
}
```

---

## Retrieve All Books

```text
GET /api/books/
```

---

## Retrieve Single Book

```text
GET /api/books/1/
```

---

## Add New Book (Admin Only)

```text
POST /api/books/
```

### Headers

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Request Body

```json
{
    "title": "Atomic Habits",
    "author": "James Clear",
    "description": "A practical guide for developing productive habits."
}
```

---

## Update Book

```text
PUT /api/books/1/
```

---

## Delete Book

```text
DELETE /api/books/1/
```

---

# ⭐ Review Endpoints

## View Book Reviews

```text
GET /api/books/1/reviews/
```

---

## Add Review

```text
POST /api/books/1/reviews/
```

### Headers

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Request Body

```json
{
    "rating": 5,
    "comment": "Excellent and very useful book."
}
```

---

## Edit Review

```text
PUT /api/reviews/1/
```

---

## Delete Review

```text
DELETE /api/reviews/1/
```

---

# 🔑 Change Password

```text
POST /api/change-password/
```

### Headers

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Request Body

```json
{
    "new_password": "newpassword123"
}
```

---

# 🖥 Admin Dashboard

Django admin panel:

```text
/admin/
```

---

# 👩‍💻 Developer

Danah Altwijri
