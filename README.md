# Book Review API

A RESTful API built using Django REST Framework (DRF).  
It allows users to register, login, browse books, and manage reviews securely using JWT authentication.

---

## Features

- User Registration & Login (JWT Authentication)
- Browse all books
- View book details
- Add reviews to books
- Edit and delete own reviews
- Admin can add, update, delete books
- Change password functionality

---

## Tech Stack

- Python 3
- Django 4+
- Django REST Framework
- SimpleJWT Authentication
- SQLite Database

---

## Authentication

This project uses JWT (JSON Web Token).

After login, include the token in all requests:

```http
Authorization: Bearer <access_token>
```

---

## API Endpoints

### Authentication

- POST `/api/register/` → Create new user
- POST `/api/token/` → Login and get JWT token
- POST `/api/token/refresh/` → Refresh token
- POST `/api/change-password/` → Change password

### Books

- GET `/api/books/` → Get all books
- POST `/api/books/` → Add book (Admin only)
- GET `/api/books/<id>/` → Get book details
- PUT `/api/books/<id>/` → Update book (Admin only)
- DELETE `/api/books/<id>/` → Delete book (Admin only)

### Reviews

- POST `/api/books/<book_id>/reviews/` → Add review
- GET `/api/books/<book_id>/reviews/` → Get reviews
- PUT `/api/reviews/<id>/` → Edit review
- DELETE `/api/reviews/<id>/` → Delete review

---

## How to Run the Project

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## Testing Tools

You can test the API using:

- Postman
- curl
- Django REST Framework browsable API

---

## Project Description

This project demonstrates how to build a secure REST API using Django REST Framework with:

- Authentication (JWT)
- Role-based permissions (Admin/User)
- CRUD operations
- Relational database design (Books & Reviews)

---

## Author
Yara Abdulrahim
