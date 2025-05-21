# Recipe-app-api
Recipe API project using Python and containerised In docker
# 🍲 Recipe App API

This project is a RESTful API for managing recipes, built using **Django** and **Django REST Framework**. It includes features like user authentication, recipe creation, tagging, and uploading images. The app is fully containerized with Docker and includes browsable API documentation via Swagger.

---

## 🚀 Features

- User registration and token-based authentication
- Create, update, delete recipes
- Upload recipe images
- Add tags and ingredients to recipes
- RESTful endpoints with DRF
- Browsable and interactive Swagger docs
- Containerized with Docker and Docker Compose

---

## 🛠️ Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/skr42/recipe-app-api.git
cd recipe-app-api
```
### Build and Start the Containers
```
docker-compose up --build
```
3. Apply Migrations
 ```
docker-compose exec web python manage.py migrate
```
4. Create Superuser (optional)
```
docker-compose exec web python manage.py createsuperuser
```
### 📋 API Documentation
After the server is running, visit:
```
http://127.0.0.1:8000/api/docs/
```

![image](https://github.com/user-attachments/assets/c2693e39-0c3e-4cb4-b02a-62f0ac2905a3)

![image](https://github.com/user-attachments/assets/17293273-a09a-4341-833e-b006534d2902)

