# Multilingual FAQ System

A Django-based FAQ system with multilingual support (English, Hindi, and Bengali), featuring a WYSIWYG editor, caching, and Dockerized deployment. The system leverages the Google Translate API for automatic translations.

## Features

- **Multilingual Support**
  - Full support for English, Hindi, and Bengali
  - Automatic translations via Google Translate API
  - Language selection through API parameters

- **Rich Content Management**
  - WYSIWYG Editor for FAQ answers
  - Django Admin integration for content management
  - Rich text formatting support

- **Technical Infrastructure**
  - REST API with language selection
  - Redis caching for optimized performance
  - PostgreSQL database backend
  - Dockerized deployment

## Installation & Setup

### Option 1: Using Docker Compose (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/saptarshi11/Multilingual_FAQ_System
   cd Multilingual_FAQ_System
   ```

2. Start the application:
   ```bash
   docker-compose up --build
   ```

### Option 2: Using Pre-built Docker Image

```bash
docker pull saptarshi11/faq-project:latest
docker run -p 8000:8000 saptarshi11/faq-project
```

## Accessing the Application

Once running, you can access:
- API Endpoint: `http://127.0.0.1:8000/api/faqs/`
- Admin Panel: `http://127.0.0.1:8000/admin/`

### Admin Access
- URL: `http://127.0.0.1:8000/admin/`
- Default credentials:
  - Username: `admin`
  - Password: `12345`

## API Usage

### Fetch FAQs in Different Languages

```bash
# English (default)
curl http://127.0.0.1:8000/api/faqs/

# Hindi
curl http://127.0.0.1:8000/api/faqs/?lang=hi

# Bengali
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

## Docker Deployment Guide

1. Ensure Docker and Docker Compose are installed
2. Navigate to project directory:
   ```bash
   cd faq_project
   ```

3. Build and start containers:
   ```bash
   docker-compose up --build -d
   ```

4. Apply database migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. Create admin user:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. View logs (optional):
   ```bash
   docker-compose logs -f
   ```

## Testing

Run tests within Docker container:
```bash
docker exec -it faq-app python manage.py test
```

## Author

Developed by **Saptarshi Mukherjee**

📧 Email: saptarshimukherjee5300@gmail.com
🔗 LinkedIn: [Saptarshi Mukherjee](https://www.linkedin.com/in/saptarshi-mukherjee-a37935238/)

