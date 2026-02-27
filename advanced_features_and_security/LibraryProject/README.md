# LibraryProject

A Django project demonstrating advanced features and security with a custom user model and role-based permissions.

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the server: `python manage.py runserver`

## Features
- Custom user model (`bookshelf.CustomUser`)
- Book model with custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)
- Role-based access control (Viewer, Editor, Admin)
- Permission-protected views

## Testing
Run:
```bash
python manage.py test bookshelf




## Security Measures Implemented
- DEBUG set to False in production
- Browser protections: XSS filter, clickjacking protection, content type nosniff
- Cookies secured with HTTPS (CSRF_COOKIE_SECURE, SESSION_COOKIE_SECURE)
- CSRF tokens included in all forms
- Safe ORM queries used to prevent SQL injection
- Input validated via Django forms
- Content Security Policy (CSP) enforced via django-csp middleware




## Security Enhancements

- Enforced HTTPS with SECURE_SSL_REDIRECT
- Configured HSTS for one year with preload and subdomains
- Secure cookies (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
- Added secure headers (X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF, SECURE_BROWSER_XSS_FILTER)
- Deployment configured with SSL/TLS certificates via Nginx
