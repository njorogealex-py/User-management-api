# User Management System

A backend API system built with Python, FastAPI, SQLAlchemy ORM and PostgreSQL that implements role based access control for multi-user industrial environments, enabling secure and structured feature restrictions across Admin, Standard and Premium user roles designed to serve as the authentication and authorization backbone for PDA device management in industrial settings, ensuring that only authorized personnel access the right features at the right level.

---

## Problem Statement

In many industrial environments, multiple workers across different responsibility levels share access to the same devices and features with no restrictions. This creates security risks, accidental data exposure and a lack of accountability. This system solves that by introducing structured role based access control enforced at the API level. 

---

## Features

- User registration with secure bcrypt password hashing
- JWT token based authentication
- Role based access control across three user levels
- Protected endpoints enforced via FastAPI dependency injection
- Admin dashboard for full user management
- Auto generated interactive API documentation
- PostgreSQL database with SQLAlchemy ORM

---

## Tech Stack

|   Technology      |           Purpose                 |
|-------------------|-----------------------------------|
| Python            | Core programming language         |
| FastAPI           | API framework                     |
| SQLAlchemy ORM    | Database abstraction layer        |  
| PostgreSQL        | Production database               |
| JWT (python-jose) | Token based authentication        |
| bcrypt (passlib)  | Password hashing                  |
| Pydantic          | Data validation and serialization |
| Uvicorn           | ASGI server                       |

---

## Role Permissions

| Feature                | Standard | Premium | Admin |
|------------------------|---------|---------|-------|
| Register               |   ✅    |   ✅   |  ✅  |
| Login                  |   ✅    |   ✅   |  ✅  |
| View own profile       |   ✅    |   ✅   |  ✅  |
| View all users         |   ❌    |   ❌   |  ✅  |
| Update user roles      |   ❌    |   ❌   |  ✅  |
| Deactivate users       |   ❌    |   ❌   |  ✅  |
| Delete users           |   ❌    |   ❌   |  ✅  |
| Access premium features|   ❌    |   ✅   |  ✅  | 


---

## Project Structure
user_management/
├── app/
│   ├── init.py
│   ├── main.py           # FastAPI app entry point
│   ├── database.py       # PostgreSQL connection and session management
│   ├── models.py         # SQLAlchemy database models
│   ├── schemas.py        # Pydantic request and response schemas
│   ├── auth.py           # Password hashing and JWT token logic
│   ├── dependencies.py   # Role based access control dependencies
│   └── routers/
│       ├── init.py
│       ├── users.py      # Register, login and profile endpoints
│       └── admin.py      # Admin only endpoints
├── .env                  # Environment variables (not pushed to GitHub)
├── requirements.txt      # Project dependencies
└── README.md

---

## Setup and Installation

### Prerequisites
- Python 3.10+
- PostgreSQL installed and running

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/user_management.git
cd user_management
```

### Step 2: Create and activate virtual environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
python -m pip install -r requirements.txt --only-binary=:all:
```

### Step 4: Configure environment variables
Create a `.env` file in the root folder:
```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/user_management
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Step 5: Create the PostgreSQL database
```bash
psql -U postgres
CREATE DATABASE user_management;
\q
```

### Step 6: Run the server
```bash
python -m uvicorn app.main:app --reload
```

### Step 7: Open the API docs
http://127.0.0.1:8000/docs

---

## API Endpoints
### Auth
| Method |   Endpoint       |        Description          | Auth Required |
|--------|------------------|-----------------------------|---------------|
| POST   | `/auth/register` |  Register a new user        | No            | 
| POST   | `/auth/login`    | Login and receive JWT token | No            |

### Users
| Method |          Endpoint        |        Description       |   Auth Required |
|--------|--------------------------|--------------------------|-----------------|
| GET    | `/users/me`              | Get current user profile |     Any role    |
| GET    |`/users/premium-feature`  | Access premium content   | Premium + Admin |

### Admin
| Method |            Endpoint            |   Description    | Auth Required |
|--------|--------------------------------|------------------|---------------|
| GET    | `/admin/users`                 | List all users   |     Admin     |
| GET    | `/admin/users/{id}`            | Get user by ID   |     Admin     |
| PATCH  | `/admin/users/{id}/role`       | Update user role |     Admin     |
| PATCH  | `/admin/users/{id}/deactivate` | Deactivate user  |     Admin     |
| DELETE | `/admin/users/{id}`            | Delete user      |     Admin     |

---

## Authentication

This API uses JWT Bearer token authentication. After logging in:

1. Copy the `access_token` from the login response
2. Click the **Authorize** button on the `/docs` page
3. Paste the token and click **Authorize**
4. All protected endpoints are now accessible based on your role

Or in Postman:
1. Go to the **Authorization** tab
2. Select **Bearer Token**
3. Paste your token

---

## Real World Application

This system is designed with industrial PDA device environments in mind where workers across different responsibility levels require different levels of access. The role based system ensures:

- **Standard workers** only access features relevant to their tasks
- **Supervisors (Premium)** gain access to restricted reporting and approval features  
- **Admins** have full control over user management and system configuration
- **Lost or stolen devices** can be instantly deactivated without physical intervention
- **Role changes** take effect immediately without device reconfiguration

---

## Author

Built as part of an industrial attachment project demonstrating backend API development with Python, FastAPI and PostgreSQL.
