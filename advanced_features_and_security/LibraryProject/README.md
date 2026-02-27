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
