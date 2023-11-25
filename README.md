# Store User data app
---
This project leverages Django Rest Framework to manage user registration and information for both parents and their children. Parents and children can be registered, and CRUD operations are available for creating, updating, listing, and deleting users. Children must have their parents registered before being added to the system. JWT authentication is implemented for future features, and Swagger is used for API documentation.
## Features
1. User Registration: Parents and children can register in the system.
2. CRUD Operations: Create, read, update, and delete operations for both parent and child users.
3. Parent-Child Relationship: Children can only be added if their parents are registered. Parents have addrress fields to add but children users do not have that.
4. JWT Authentication: Implemented for secure user authentication and authorization.
5. API Documentation: Swagger is used for clear and interactive API documentation.

## Installation
### Clone the Repository:
   git clone https://github.com/sami1310/user-data-app.git

### Create Virtual Environment
python -m venv venv

#### Activate on Windows
venv\Scripts\activate
####  On Unix or MacOS
source venv/bin/activate

### Install Dependencies
cd user_data_app

pip install -r requirements.txt

### Apply Database Migrations
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

### Run the Development Server:

python manage.py runserver

Access the application at http://127.0.0.1:8000. (Windows)

Access the application at http://localhost:8000/. (Linux)

### Access Swagger Documentation
http://127.0.0.1:8000/api/docs

1. Create/Register Parent user at parent/register
2. Update Parent user at parent/{uid}  (parent uid)
3. Get list of all Parents users at parent
4. Delete Parent user at parent/delete/{uid} (user uid)
5. Create/Register Child user at child/register
6. Update Child user at child/{uid}  (child uid)
7. Get list of all Child users at child
8. Delete Child user at Child/delete/{uid} (user uid)