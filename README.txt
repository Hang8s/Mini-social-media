# Mini Social Media

A simple mini social media web application built with Python and Django.

---

### 🚀 Overview

Mini Social Media is a basic social networking platform where users can:

- Register and log in
- Create posts with text and images
- View posts from all users
- Browse user profiles
- Like and comment on posts 
- Search posts

### 🧱 Features

- User authentication (signup, login, logout)  
- Post creation with optional media (images)  
- Homepage feed of all posts  
- User profiles  
- Static file handling (CSS + images)  
- PostgreSQL database  

### 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django (Python) |
| Database | PostgreSQL |
| Frontend | HTML, CSS, Django Templates, Htmx , Tailwind  |
| Static Files | Django Static |

### 📦 Installation & Launch

1. **Clone the repository**

   git clone https://github.com/Hang8s/Mini-social-media.git
   cd Mini-social-media
Create a virtual environment

python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
Install dependencies


pip install -r requirements.txt
Configure PostgreSQL

Create a database and user do it at pgadmin4:


CREATE DATABASE mini_social_db;
CREATE USER mini_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE mini_social_db TO mini_user;
Update settings.py DATABASES section:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mini_social_db',
        'USER': 'mini_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Run migrations


python manage.py migrate
Create superuser (optional)


python manage.py createsuperuser
Start the development server


python manage.py runserver
Open in browser


http://localhost:8000
🧩 Project Structure


Mini-social-media/
├── core/                 # main Django app
├── media/                # uploaded media
├── static/               # CSS and JS
├── templates/            # HTML templates
├── manage.py             # Django CLI entrypoint
└── requirements.txt      # python dependencies
🤝 Contributing
Fork the project

Create a feature branch (git checkout -b feature/foo)

Commit your changes

Push to your fork

Submit a Pull Request

📄 License
This project is open source and available under the MIT License.
